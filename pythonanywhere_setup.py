#!/usr/bin/env python
"""
PythonAnywhere setup script for the MUK Support Portal backend.
This script helps set environment variables and configure the application on PythonAnywhere.
"""

import os
import sys
import getpass

def main():
    print("PythonAnywhere Setup for MUK Support Portal Backend")
    print("==================================================")
    
    # Get PythonAnywhere username
    username = input("Enter your PythonAnywhere username: ")
    
    # Get DB password
    db_password = getpass.getpass("Enter your MySQL database password: ")
    
    # Get frontend domain if applicable
    use_frontend = input("Do you have a frontend application domain? (y/n): ").lower() == 'y'
    frontend_domain = ""
    if use_frontend:
        frontend_domain = input("Enter the frontend domain (e.g., https://myapp.com): ")
    
    # Create .env file with these values
    env_content = f"""
# PythonAnywhere Configuration
PA_USERNAME={username}
PA_DB_PASSWORD={db_password}
PYTHONANYWHERE_DOMAIN=1
"""
    
    if frontend_domain:
        env_content += f"FRONTEND_DOMAIN={frontend_domain}\n"
    
    # Write to .env file
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("\nConfiguration saved to .env file.")
    print("\nNext steps:")
    print("1. Make sure you've created a MySQL database on PythonAnywhere")
    print(f"2. The database name should be: {username}$muk_support_portal")
    print("3. Run 'python manage.py migrate' to set up the database")
    print("4. Run 'python manage.py createsuperuser' to create an admin user")
    print("5. Run 'python manage.py collectstatic' to collect static files")
    print("6. Configure your web app on PythonAnywhere to point to this directory")
    print("\nEdit your WSGI file to include:")
    print(f"""
import os
import sys

path = '/home/{username}/tracker-backend'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'muk_support_backend.settings'

# Load environment variables from .env
from dotenv import load_dotenv
project_folder = os.path.expanduser(path)
load_dotenv(os.path.join(project_folder, '.env'))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
""")

if __name__ == "__main__":
    main() 