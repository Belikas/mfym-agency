# Lanceur des runs planifiés de l'agence. Appelé par le Planificateur de tâches Windows.
# Usage : run.ps1 -Goal <nom> [-MaxTurns 60] [-TimeoutMin 45] [-Model opus]
param(
  [Parameter(Mandatory)] [string]$Goal,
  [int]$MaxTurns = 60,
  [int]$TimeoutMin = 45,
  [string]$Model = "opus",
  [switch]$HoldLockTest   # test : tient le verrou 90 s sans lancer Claude
)
$ErrorActionPreference = "Stop"
$Root    = "C:\Users\Baptiste\Desktop\CLAUDE CODE\MAKE FUCK YOU MONEY INC"
$Claude  = "C:\Users\Baptiste\AppData\Roaming\npm\claude.cmd"
$Python  = "C:\Users\Baptiste\miniconda3\python.exe"
$RunDir  = Join-Path $Root "run"
$LogDir  = Join-Path $Root "logs"
$Lock    = Join-Path $RunDir "agency.lock"
$RunLog  = Join-Path $LogDir "runs.jsonl"
$State   = Join-Path $RunDir "failures.txt"
New-Item -ItemType Directory -Force $RunDir, $LogDir | Out-Null
Set-Location $Root

function Write-RunLog($obj) {
  $obj.ts = (Get-Date).ToString("s")
  [IO.File]::AppendAllText($RunLog, ($obj | ConvertTo-Json -Compress) + "`n")
}
function Send-Alert($text) {
  & $Python (Join-Path $Root "scripts\tg.py") alert $text
}

# 1. Verrou : un seul run à la fois. Verrou d'un processus mort ou de plus de 2 h = périmé.
# La revue hebdo n'a pas de rattrapage : elle attend jusqu'à 30 min que le verrou se libère
# (puis raccourcit son timeout d'autant pour rester sous la limite du planificateur, 70 min).
if ($Goal -eq "hebdo") {
  $waited = 0
  while ((Test-Path $Lock) -and $waited -lt 30) {
    $lockPid = [int](Get-Content $Lock -ErrorAction SilentlyContinue)
    if (-not ($lockPid -and (Get-Process -Id $lockPid -ErrorAction SilentlyContinue))) { break }
    Start-Sleep 60; $waited++
  }
  if ($waited) { $TimeoutMin = [Math]::Max(20, $TimeoutMin - $waited) }
}
if (Test-Path $Lock) {
  $age = (Get-Date) - (Get-Item $Lock).LastWriteTime
  $lockPid = [int](Get-Content $Lock -ErrorAction SilentlyContinue)
  $alive = $lockPid -and (Get-Process -Id $lockPid -ErrorAction SilentlyContinue)
  if ($alive -and $age.TotalMinutes -lt 120) {
    Write-RunLog @{ goal = $Goal; status = "skipped_locked"; holder = "$lockPid" }
    exit 0
  }
  Remove-Item $Lock -Force
}
Set-Content -Path $Lock -Value $PID

try {
  if ($HoldLockTest) { Start-Sleep 90; Write-RunLog @{ goal = $Goal; status = "lock_test_done" }; return }

  # 2. Environnement : secrets depuis .env ; jamais de clé API (elle facturerait l'API au lieu du forfait Max).
  Get-Content (Join-Path $Root ".env") | Where-Object { $_ -match '^\s*([A-Z_]+)=(.+)$' } | ForEach-Object {
    [Environment]::SetEnvironmentVariable($Matches[1], $Matches[2].Trim(), "Process")
  }
  Remove-Item Env:ANTHROPIC_API_KEY -ErrorAction SilentlyContinue
  Remove-Item Env:ANTHROPIC_AUTH_TOKEN -ErrorAction SilentlyContinue
  $env:CLAUDE_CODE_GIT_BASH_PATH = "C:\Program Files\Git\bin\bash.exe"
  $env:DISABLE_AUTOUPDATER = "1"
  $runId = "{0}-{1}" -f (Get-Date -Format "yyyyMMdd-HHmm"), $Goal
  $env:MFYM_RUN_ID = $runId
  $env:MFYM_AGENT = "directeur"

  $goalFile = Join-Path $Root "prompts\$Goal.md"
  if (-not (Test-Path $goalFile)) { throw "prompt introuvable : $goalFile" }
  $promptFile = Join-Path $RunDir "prompt-$Goal.md"
  $combined = (Get-Content (Join-Path $Root "prompts\_commun.md") -Raw -Encoding utf8) + "`n# Objectif de ce run : $Goal`n" + (Get-Content $goalFile -Raw -Encoding utf8)
  [IO.File]::WriteAllText($promptFile, $combined)
  $out = Join-Path $LogDir "$runId.json"
  $err = Join-Path $LogDir "$runId.err.txt"

  # 3. Run headless : mode dontAsk + liste d'outils ; le hook guard.py bloque le reste.
  $cargs = @("-p", "--model", $Model, "--max-turns", "$MaxTurns", "--output-format", "json",
             "--permission-mode", "dontAsk",
             "--allowedTools", "Bash,PowerShell,Read,Write,Edit,Glob,Grep,WebSearch,WebFetch,Agent,Skill",
             "--append-system-prompt-file", "`"$promptFile`"",
             "`"Execute le run $Goal decrit dans ton prompt systeme. Run id : $runId.`"")
  $start = Get-Date
  $p = Start-Process -FilePath $Claude -ArgumentList $cargs -NoNewWindow -PassThru `
        -RedirectStandardOutput $out -RedirectStandardError $err -WorkingDirectory $Root
  $null = $p.Handle   # sans ça, ExitCode reste vide avec WaitForExit(timeout)
  if (-not $p.WaitForExit($TimeoutMin * 60 * 1000)) {
    & taskkill /PID $p.Id /T /F | Out-Null
    $status = "timeout"
  } else {
    $status = if ($p.ExitCode -eq 0) { "ok" } else { "error" }
  }
  $text = "$(Get-Content $out -Raw -ErrorAction SilentlyContinue)$(Get-Content $err -Raw -ErrorAction SilentlyContinue)"
  if ($text -match "hit your (session|weekly|Opus|Sonnet) limit") { $status = "quota" }
  elseif ($text -match "Failed to authenticate|Invalid API key|Invalid authentication credentials|Please run /login") { $status = "auth" }
  if ($text -match "Warning: this sign-in") { Send-Alert "Le token Claude expire bientot : relance 'claude setup-token' et mets-le dans .env." }

  $minutes = [math]::Round(((Get-Date) - $start).TotalMinutes, 1)
  Write-RunLog @{ goal = $Goal; run_id = $runId; status = $status; minutes = $minutes; exit = $p.ExitCode }

  # 4. Alertes : auth tout de suite, sinon 2 échecs de suite. Le quota n'est pas un échec.
  $fails = [int](Get-Content $State -ErrorAction SilentlyContinue)
  if ($status -in @("ok", "quota")) { $fails = 0 } else { $fails++ }
  Set-Content $State $fails
  if ($status -eq "auth") { Send-Alert "Run $Goal : echec d'authentification Claude. Refais 'claude setup-token' et mets le token dans .env." }
  elseif ($fails -ge 2) { Send-Alert "2 runs de suite en echec (dernier : $Goal, $status). Logs : logs\$runId.err.txt" }
}
catch {
  Write-RunLog @{ goal = $Goal; status = "wrapper_error"; error = "$_" }
  Send-Alert "Lanceur en erreur ($Goal) : $_"
}
finally {
  Remove-Item $Lock -Force -ErrorAction SilentlyContinue
}
