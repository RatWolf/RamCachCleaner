# Pfad zu RamMap.exe
$ramMapPath = "C:\Program Files\Rammap\RamMap64.exe"

$memoryInfo = Get-CimInstance -ClassName Win32_PerfRawData_PerfOS_Memory

$freeMemoryGB = [math]::Round($memoryInfo.AvailableBytes / 1GB, 2)

$standbyMemoryBytes = $memoryInfo.StandbyCacheReserveBytes + $memoryInfo.StandbyCacheNormalPriorityBytes + $memoryInfo.StandbyCacheCoreBytes
$standbyMemoryGB = [math]::Round($standbyMemoryBytes / 1GB, 2)

$unusedMemoryGB = $freeMemoryGB - $standbyMemoryGB

# Funktion zum Extrahieren des Speicherwerts in GB
function Get-MemoryValueGB {
    param (
        [string]$pattern
    )
    
    $line = $output | Select-String -Pattern $pattern
    if ($line) {
        $value = [double]($line -replace $pattern, "") -replace " MB", ""
        return [math]::Round($value / 1024, 2)
    } else {
        return 0
    }
}

Write-Host "Unused RAM: $unusedMemoryGB GB"
Write-Host "Standby RAM: $standbyMemoryGB GB"

# Wenn Unused Memory unter 1GB liegt, Standby Speicher leeren
if ($unusedMemoryGB -lt 1) {
    Write-Host "Unused RAM ist unter 1GB. Leere Standby Speicher..."
    & $ramMapPath -Ew -Es -Em -Et -E0
    Write-Host "Standby Speicher geleert."
} else {
    Write-Host "Unused RAM ist über 1GB. Keine Aktion erforderlich."
}