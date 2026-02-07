$ErrorActionPreference = 'Stop'

$sourceRoot = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$capstoneRoot = Split-Path $PSScriptRoot -Parent
$sourceCode = Join-Path $capstoneRoot 'code'
$sourceData = Join-Path $capstoneRoot 'data'
$destCode = Join-Path $sourceRoot 'uwf-idc6940-capstone-files\code'
$destData = Join-Path $sourceRoot 'uwf-idc6940-capstone-files\data'

if (-not (Test-Path -LiteralPath $destCode)) {
    New-Item -ItemType Directory -Path $destCode -Force | Out-Null
}
if (-not (Test-Path -LiteralPath $destData)) {
    New-Item -ItemType Directory -Path $destData -Force | Out-Null
}

$copies = @(
    @{ Source = 'time_series_forecast_final.qmd'; Dest = 'arima_forecast.qmd' }
    @{ Source = 'lstm_forecast_final.qmd'; Dest = 'lstm_forecast.qmd' }
    @{ Source = 'time_series_forecast_final.html'; Dest = 'arima_forecast_qmd_output.html' }
    @{ Source = 'lstm_forecast_final.html'; Dest = 'lstm_forecast_qmd_output.html' }
)

$dataCopies = @(
    @{ Source = 'finalproject.csv'; Dest = 'time_series.csv' }
    @{ Source = 'arima_forecast_14day.csv'; Dest = 'arima_forecast_14day.csv' }
    @{ Source = 'lstm_forecast_14day.csv'; Dest = 'lstm_forecast_14day.csv' }
)

foreach ($item in $copies) {
    $srcPath = Join-Path $sourceCode $item.Source
    if (-not (Test-Path -LiteralPath $srcPath)) {
        Write-Warning "Source not found: $srcPath"
        continue
    }
    $destPath = Join-Path $destCode $item.Dest
    Copy-Item -LiteralPath $srcPath -Destination $destPath -Force
    Write-Host "Copied $($item.Source) -> $destCode\$($item.Dest)"
}

foreach ($item in $dataCopies) {
    $srcPath = Join-Path $sourceData $item.Source
    if (-not (Test-Path -LiteralPath $srcPath)) {
        Write-Warning "Source not found: $srcPath"
        continue
    }
    $destPath = Join-Path $destData $item.Dest
    Copy-Item -LiteralPath $srcPath -Destination $destPath -Force
    Write-Host "Copied $($item.Source) -> $destData\$($item.Dest)"
}

Write-Host "Done."
