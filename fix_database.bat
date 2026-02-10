@echo off
echo 🚀 Fixing Database Migration Issues...
echo.

REM Change to the correct directory
cd /d "c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto"

echo 1. Activating virtual environment...
call venv\Scripts\activate.bat

echo 2. Creating migration file...
python manage.py makemigrations crypto --name add_missing_fields --empty

echo 3. Applying migrations...
python manage.py migrate crypto

echo 4. Seeding ranks...
python manage.py seed_ranks

echo.
echo ✅ Migration fix completed!
echo.
echo Now try running the server again:
echo python manage.py runserver
echo.
pause
