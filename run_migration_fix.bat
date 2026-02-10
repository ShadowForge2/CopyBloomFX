@echo off
echo 🚀 Starting Database Migration Fix...
echo.

REM Run the migration fix script
python fix_migrations.py

echo.
echo Press any key to exit...
pause > nul
