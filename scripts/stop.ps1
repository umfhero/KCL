$ErrorActionPreference='Stop'
$studyData=if($env:KCL_STUDY_DATA){$env:KCL_STUDY_DATA}else{Join-Path $env:USERPROFILE 'Desktop\KCL\study-data'}
$studyRecord=Join-Path $studyData 'server-process.json'
if(-not(Test-Path -LiteralPath $studyRecord)){Write-Output 'No saved study app process.';exit 0}
$studySaved=Get-Content -LiteralPath $studyRecord | ConvertFrom-Json
$studyProcess=Get-Process -Id $studySaved.pid -ErrorAction SilentlyContinue
if(-not $studyProcess){Write-Output 'Study app is already stopped.';exit 0}
if($studyProcess.StartTime.ToUniversalTime().Ticks -ne ([datetime]$studySaved.started).ToUniversalTime().Ticks){throw 'The saved process ID has been reused. No process was stopped.'}
$studyCommand=(Get-CimInstance Win32_Process -Filter "ProcessId=$($studySaved.pid)").CommandLine
if($studyCommand -notmatch '-m server.main'){throw 'The saved process is not the study app. No process was stopped.'}
$studyChildren=Get-CimInstance Win32_Process -Filter "ParentProcessId=$($studySaved.pid)"
foreach($studyChild in $studyChildren){
    if($studyChild.Name -eq 'codex.exe' -and $studyChild.CommandLine -match 'app-server'){
        Stop-Process -Id $studyChild.ProcessId -ErrorAction SilentlyContinue
    }
}
Stop-Process -Id $studySaved.pid
Write-Output 'KCL study space stopped.'
