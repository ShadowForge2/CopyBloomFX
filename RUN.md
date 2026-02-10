# Test the Django crypto app right now

## Option 1: PowerShell (recommended if you saw venv activation errors)

The venv lives **inside `django_crypto`**, not at project root. Use a **relative path** to avoid issues with `1`030` in your user path:

```powershell
cd django_crypto
.\run.ps1
```

If you get *"script cannot be loaded because running scripts is disabled"*:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then run `.\run.ps1` again.

## Option 2: CMD / `run.bat`

```cmd
cd django_crypto
run.bat
```

## Option 3: Manual activate (PowerShell)

```powershell
cd django_crypto
python -m venv venv
.\venv\Scripts\Activate.ps1    # relative path — don't use full path with 1`030
pip install -r requirements.txt
python manage.py makemigrations crypto
python manage.py migrate
python manage.py seed
python manage.py runserver
```

## Then

1. Open **http://127.0.0.1:8000**
2. Login: **admin** / **admin123**
3. Or sign up and use Dashboard, Finance, Profile, Referral, Admin.
