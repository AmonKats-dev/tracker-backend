# Fixing MySQL Connection Error on PythonAnywhere

If you're encountering the error:

```
django.db.utils.OperationalError: (2002, "Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)")
```

This means Django is trying to connect to a local MySQL server using a socket file, but PythonAnywhere's MySQL service doesn't use socket files for connections.

## Solution

### Option 1: Quick Manual Fix

1. Open a Bash console on PythonAnywhere
2. Create a `.env` file with your database credentials:

```bash
cd ~/tracker-backend
echo "PA_USERNAME=yourusername" > .env
echo "PA_DB_PASSWORD=yourdatabasepassword" >> .env
echo "PYTHONANYWHERE_DOMAIN=1" >> .env
```

Replace `yourusername` with your actual PythonAnywhere username and `yourdatabasepassword` with your database password.

3. Make sure you've created a MySQL database in the PythonAnywhere "Databases" tab
4. The database name should follow this format: `yourusername$muk_support_portal`

### Option 2: Use the Setup Script

We've included a setup script that will handle this configuration for you:

```bash
cd ~/tracker-backend
python pythonanywhere_setup.py
```

Follow the prompts to enter your information.

### Option 3: Edit settings.py Directly

If needed, you can directly edit the settings:

```bash
cd ~/tracker-backend
nano muk_support_backend/settings.py
```

Find the DATABASES section and modify it to use:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourusername$muk_support_portal',
        'USER': 'yourusername',
        'PASSWORD': 'your-database-password',
        'HOST': 'yourusername.mysql.pythonanywhere-services.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'",
            'charset': 'utf8',
            'use_unicode': True,
        }
    }
}
```

Replace all instances of `yourusername` with your actual PythonAnywhere username and `your-database-password` with your actual database password.

## After Fixing the Database Connection

Once you've applied one of these fixes, try running migrations again:

```bash
python manage.py migrate
```

This should now successfully connect to your PythonAnywhere MySQL database and run migrations. 