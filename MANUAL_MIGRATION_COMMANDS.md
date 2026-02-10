# Manual Migration Commands

## Step 1: Open Command Prompt or PowerShell as Administrator
## Navigate to the project directory:
cd "c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto"

## Step 2: Activate virtual environment (if using venv)
venv\Scripts\activate

## Step 3: Run Django migrations
python manage.py makemigrations
python manage.py migrate

## Step 4: Seed the ranks
python manage.py seed_ranks

## Step 5: Create admin user (if needed)
python manage.py createsuperuser

## Alternative: If the above doesn't work, try these commands directly:

### Create migration manually
python manage.py makemigrations crypto --name update_rank_and_profile_fields

### Apply migration
python manage.py migrate crypto

### Check migration status
python manage.py showmigrations crypto
