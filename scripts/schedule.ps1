# Enregistre (ou remet à jour) toutes les tâches planifiées de l'agence. Idempotent.
# Admin (recommandé) : tourne sans session ouverte (S4U) et démarre au boot.
# -NoAdmin : tourne seulement quand Baptiste a une session ouverte ; services lancés à l'ouverture de session.
param([switch]$NoAdmin)
$ErrorActionPreference = "Stop"
$Root  = "C:\Users\Baptiste\Desktop\CLAUDE CODE\MAKE FUCK YOU MONEY INC"
$Py     = "C:\Users\Baptiste\miniconda3\pythonw.exe"
$PS     = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
$User   = "$env:USERDOMAIN\$env:USERNAME"
# S4U : tourne même sans session ouverte (après une coupure de courant), sans stocker de mot de passe.
$Principal = if ($NoAdmin) { New-ScheduledTaskPrincipal -UserId $User -LogonType Interactive -RunLevel Limited }
             else { New-ScheduledTaskPrincipal -UserId $User -LogonType S4U -RunLevel Limited }

function Set-AgencyTask($Name, $Trigger, $Exe, $Arguments, [int]$LimitMin = 60, [switch]$Service) {
  $action = New-ScheduledTaskAction -Execute $Exe -Argument $Arguments -WorkingDirectory $Root
  $settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -WakeToRun -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries -MultipleInstances IgnoreNew `
    -ExecutionTimeLimit ([TimeSpan]::FromMinutes($LimitMin)) `
    -RestartCount 999 -RestartInterval ([TimeSpan]::FromMinutes(1))
  if ($Service) { $settings.ExecutionTimeLimit = "PT0S" }
  # Pas de -TaskPath : un sous-dossier exige l'admin.
  Register-ScheduledTask -TaskName $Name -Action $action -Trigger $Trigger `
    -Principal $Principal -Settings $settings -Force | Out-Null
  "OK $Name"
}

$run = { param($goal, $model, $turns, $min) "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$Root\scripts\run.ps1`" -Goal $goal -Model $model -MaxTurns $turns -TimeoutMin $min" }

Set-AgencyTask "MFYM-quotidien-0730" (New-ScheduledTaskTrigger -Daily -At 07:30) $PS (& $run quotidien opus 60 45) 55
Set-AgencyTask "MFYM-quotidien-1300" (New-ScheduledTaskTrigger -Daily -At 13:00) $PS (& $run quotidien sonnet 60 45) 55
Set-AgencyTask "MFYM-quotidien-1900" (New-ScheduledTaskTrigger -Daily -At 19:00) $PS (& $run quotidien sonnet 60 45) 55
Set-AgencyTask "MFYM-hebdo"          (New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 10:00) $PS (& $run hebdo opus 80 60) 70
Set-AgencyTask "MFYM-digest"         (New-ScheduledTaskTrigger -Daily -At 20:30) $Py "`"$Root\scripts\tg.py`" digest" 5
Set-AgencyTask "MFYM-backup"         (New-ScheduledTaskTrigger -Daily -At 03:00) $Py "`"$Root\scripts\maint.py`" backup" 10
$hb = New-ScheduledTaskTrigger -Once -At (Get-Date).Date -RepetitionInterval ([TimeSpan]::FromMinutes(5))
Set-AgencyTask "MFYM-heartbeat"      $hb $Py "`"$Root\scripts\maint.py`" heartbeat" 2
$boot = if ($NoAdmin) { New-ScheduledTaskTrigger -AtLogOn -User $User } else { New-ScheduledTaskTrigger -AtStartup }
Set-AgencyTask "MFYM-bot"            $boot $Py "`"$Root\scripts\bot.py`"" -Service
Set-AgencyTask "MFYM-dashboard"      $boot $Py "`"$Root\dashboard\server.py`"" -Service
Set-AgencyTask "MFYM-startup-check"  $boot $Py "`"$Root\scripts\maint.py`" startup" 10
