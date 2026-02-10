@echo off
cd /d "%~dp0"
if not exist venv (
  echo Creating venv...
  python -m venv venv
)
call venv\Scripts\activate.bat
pip install -q -r requirements.txt
python manage.py makemigrations crypto
python manage.py migrate
python manage.py seed
echo.
echo ========================================
echo  Copy Trade - http://127.0.0.1:8000
echo  Admin: admin / admin123
echo ========================================
python manage.py runserver
