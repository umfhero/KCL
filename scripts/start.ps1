param([switch]$NoBrowser)
$ErrorActionPreference = 'Stop'
$studyRoot = Split-Path -Parent $PSScriptRoot
$studyData = if ($env:KCL_STUDY_DATA) { $env:KCL_STUDY_DATA } else { Join-Path $env:USERPROFILE 'Desktop\KCL\study-data' }
$studyPort = if ($env:KCL_PORT) { [int]$env:KCL_PORT } else { 4826 }
$studyUrl = "http://127.0.0.1:$studyPort"
New-Item -ItemType Directory -Force -Path (Join-Path $studyData 'logs') | Out-Null
try { $studyHealth = Invoke-RestMethod "$studyUrl/api/health" -TimeoutSec 2 } catch { $studyHealth = $null }
if ($studyHealth -and $studyHealth.app -eq 'kcl-study-space') {
    Write-Output "KCL study space is already running at $studyUrl"
    if (-not $NoBrowser) { Start-Process $studyUrl }
    exit 0
}
if (Get-NetTCPConnection -State Listen -LocalPort $studyPort -ErrorAction SilentlyContinue) { throw "Port $studyPort is used by another service. Set KCL_PORT to an available port." }
if (-not (Test-Path -LiteralPath (Join-Path $studyRoot 'dist\index.html'))) {
    Push-Location $studyRoot
    try { node scripts/build.mjs; if ($LASTEXITCODE -ne 0) { throw 'Dashboard build failed.' } } finally { Pop-Location }
}
$studyPython = (Get-Command python).Source
$studyProcess = Start-Process -FilePath $studyPython -ArgumentList @('-m','server.main') -WorkingDirectory $studyRoot -WindowStyle Hidden -RedirectStandardOutput (Join-Path $studyData 'logs\server.out.log') -RedirectStandardError (Join-Path $studyData 'logs\server.error.log') -PassThru
@{ pid=$studyProcess.Id; started=$studyProcess.StartTime.ToUniversalTime().ToString('o'); url=$studyUrl } | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $studyData 'server-process.json')
for ($studyAttempt=0; $studyAttempt -lt 40; $studyAttempt++) {
    Start-Sleep -Milliseconds 500
    try { $studyHealth=Invoke-RestMethod "$studyUrl/api/health" -TimeoutSec 2; if ($studyHealth.app -eq 'kcl-study-space') { break } } catch { }
    if ($studyProcess.HasExited) { throw "App failed to start. Check $studyData\logs\server.error.log" }
}
if (-not $studyHealth -or $studyHealth.app -ne 'kcl-study-space') { throw "App is still starting. Check $studyData\logs\server.error.log" }
Write-Output "KCL study space is running at $studyUrl"
if (-not $NoBrowser) { Start-Process $studyUrl }
