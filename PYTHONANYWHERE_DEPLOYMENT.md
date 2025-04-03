# Deploying to PythonAnywhere

This guide will walk you through deploying the MUK Support Portal backend to PythonAnywhere.

## Prerequisites

1. A PythonAnywhere account (free tier works for testing)
2. Basic knowledge of Python, Django, and MySQL

## Step 1: Set up PythonAnywhere

1. Sign up or log in to [PythonAnywhere](https://www.pythonanywhere.com/)
2. Open a Bash console from your dashboard

## Step 2: Clone the Repository

```bash
git clone https://github.com/AmonKats-dev/tracker-backend.git
cd tracker-backend
```

## Step 3: Create a Virtual Environment

```bash
mkvirtualenv --python=python3.10 tracker-env
workon tracker-env
```

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 5: Create a MySQL Database

1. Go to the "Databases" tab in your PythonAnywhere dashboard
2. Create a new MySQL database (e.g., `yourusername$muk_support_portal`)
3. Note your MySQL username, password, and host

## Step 6: Configure the Application

Run the setup script to configure your environment:

```bash
python pythonanywhere_setup.py
```

Follow the prompts to enter your:
- PythonAnywhere username
- MySQL database password
- Frontend application domain (if applicable)

## Step 7: Run Migrations and Create Admin User

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

## Step 8: Configure the Web App

1. Go to the "Web" tab in your PythonAnywhere dashboard
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.10

### Configure WSGI File

Click on the WSGI configuration file link and replace its contents with:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/tracker-backend'
if path not in sys.path:
    sys.path.append(path)

# Set environment variable to tell Django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'muk_support_backend.settings'

# Load environment variables from .env
from dotenv import load_dotenv
project_folder = os.path.expanduser(path)
load_dotenv(os.path.join(project_folder, '.env'))

# Import Django's WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Replace `yourusername` with your actual PythonAnywhere username.

### Configure Static Files

In the "Static files" section:
- URL: `/static/`
- Directory: `/home/yourusername/tracker-backend/static/`

For media files:
- URL: `/media/`
- Directory: `/home/yourusername/tracker-backend/media/`

## Step 9: Reload the Web App

Click the "Reload" button for your web app.

## Step 10: Test Your Deployment

Your API is now available at:
- https://yourusername.pythonanywhere.com/api/
- Admin interface: https://yourusername.pythonanywhere.com/admin/

## Troubleshooting

### Database Connection Issues

If you get database connection errors, verify:
1. The database name in your `.env` file matches the one you created
2. Your database username and password are correct
3. You have the correct host name

### Static Files Not Loading

If static files aren't loading:
1. Check your static file configuration on the web tab
2. Ensure you ran `python manage.py collectstatic`
3. Check file permissions

### Server Error (500)

If you get a 500 error:
1. Check the error logs in the "Web" tab
2. Make sure DEBUG is set to False in production
3. Verify your ALLOWED_HOSTS includes your PythonAnywhere domain 