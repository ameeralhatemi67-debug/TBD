# Bounded research observation. No login, booking, or production ingestion.
# Full HTML stays local; only response metadata and original research notes are published.
param([ValidateSet('initial','public-app','interpretation')][string]$Batch = 'initial')
$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path $PSScriptRoot -Parent
$privateDir = Join-Path $taskRoot '.local_source_checks'
New-Item -ItemType Directory -Force -Path $privateDir | Out-Null
$targets = @(
    @{ id='scitech_robots'; url='https://scitech.sa/robots.txt' },
    @{ id='scitech_price_ar'; url='https://scitech.sa/p/24' },
    @{ id='scitech_hours_ar'; url='https://scitech.sa/working-hours' },
    @{ id='scitech_hours_en'; url='https://scitech.sa/en/p/22' },
    @{ id='scitech_privacy'; url='https://scitech.sa/privacy-policy' },
    @{ id='escape_main'; url='https://www.escapetheroomsa.com/' },
    @{ id='escape_room_khobar'; url='https://www.escapetheroomsa.com/rooms/the-prison-khobar/' },
    @{ id='escape_khobar'; url='https://khobar.escapetheroomsa.com/' },
    @{ id='escape_robots'; url='https://www.escapetheroomsa.com/robots.txt' },
    @{ id='sparky_locations'; url='https://sa.sparkysme.com/Home/Locations' },
    @{ id='ithra_visit'; url='https://www.ithra.com/en/visit-ithra' },
    @{ id='ithra_terms'; url='https://www.ithra.com/en/terms-and-conditions' }
)
if ($Batch -eq 'public-app') {
    # URLs and parameter names observed in the site's public client; read-only endpoints only.
    $targets = @(
        @{id='escape_public_app'; url='https://www.escapetheroomsa.com/assets/index-CKJXdZzF.js'},
        @{id='escape_branches'; url='https://api.escapetheroomsa.com/api/branches'},
        @{id='escape_rooms1'; url='https://api.escapetheroomsa.com/api/rooms?branchId=1'},
        @{id='escape_faq'; url='https://api.escapetheroomsa.com/api/faq'},
        @{id='escape_privacy_client'; url='https://www.escapetheroomsa.com/assets/Privacy-DOYmZ1OF.js'},
        @{id='escape_slots4'; url='https://api.escapetheroomsa.com/api/availability/slots?roomId=1&date=2026-09-27&players=4'},
        @{id='route_demo'; url='https://router.project-osrm.org/route/v1/driving/50.2,26.3;50.1945561,26.3055142?overview=false'}
    )
}
if ($Batch -eq 'interpretation') {
    $targets = @(
        @{id='escape_privacy'; url='https://api.escapetheroomsa.com/api/pages/privacy'},
        @{id='escape_room_client'; url='https://www.escapetheroomsa.com/assets/RoomDetail-B3labSzF.js'},
        @{id='route_demo_return'; url='https://router.project-osrm.org/route/v1/driving/50.1945561,26.3055142;50.2,26.3?overview=false'}
    )
}
$manifestName = switch ($Batch) { 'initial' {'http_checks.json'} 'public-app' {'public_app_checks.json'} 'interpretation' {'interpretation_checks.json'} }
if (Test-Path (Join-Path $PSScriptRoot $manifestName)) { throw 'Preserve the existing dated manifest; use a new evidence directory for a later run.' }
$records = @()
foreach ($target in $targets) {
    $record = [ordered]@{id=$target.id; requested_url=$target.url; started_utc=[DateTime]::UtcNow.ToString('o'); channel='PowerShell Invoke-WebRequest, standard TLS validation'; max_timeout_seconds=20}
    $timer = [Diagnostics.Stopwatch]::StartNew()
    try {
        $response = Invoke-WebRequest -Uri $target.url -TimeoutSec 20
        $content = [string]$response.Content
        $bytes = [Text.Encoding]::UTF8.GetBytes($content)
        $record.status = [int]$response.StatusCode
        $record.final_url = $response.BaseResponse.RequestMessage.RequestUri.AbsoluteUri
        $record.content_type = [string]$response.Headers['Content-Type']
        $record.server_date = [string]$response.Headers['Date']
        $record.last_modified = [string]$response.Headers['Last-Modified']
        $record.utf8_text_bytes = $bytes.Length
        $record.sha256_utf8_decoded_content = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($bytes)).ToLowerInvariant()
        [IO.File]::WriteAllBytes((Join-Path $privateDir ($target.id+'.html')), $bytes)
    } catch {
        $record.status = if ($_.Exception.Response) { [int]$_.Exception.Response.StatusCode } else { $null }
        $record.error = $_.Exception.Message
    }
    $record.elapsed_seconds = [Math]::Round($timer.Elapsed.TotalSeconds,2)
    $record.finished_utc = [DateTime]::UtcNow.ToString('o')
    $records += $record
    $records | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 (Join-Path $PSScriptRoot $manifestName)
    Write-Output ($target.id+' status='+$record.status+' seconds='+$record.elapsed_seconds)
}
