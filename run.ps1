# Run Django crypto app from PowerShell.
# Run from django_crypto folder:  cd django_crypto; .\run.ps1
# If you get "script cannot be loaded":  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Set-Location $PSScriptRoot

if (-not (Test-Path venv)) {
    Write-Host "Creating venv..."
    python -m venv venv
}
. .\venv\Scripts\Activate.ps1
pip install -q -r requirements.txt
python manage.py makemigrations crypto 2>$null; python manage.py migrate
python manage.py seed
Write-Host ""
Write-Host "========================================"
Write-Host " Copy Trade - http://127.0.0.1:8000"
Write-Host " Admin: admin / admin123"
Write-Host "========================================"
python manage.py runserver
