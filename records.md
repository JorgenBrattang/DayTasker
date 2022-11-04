# Walk-through to how I built my Website.
*(This will not cover everything, like every detail within the HTML and CSS)*
First we need to install a few things to start the project.

## Install Django
```
pip3 install 'django<4' gunicorn
```

## Install Bootstrap
```
pip install crispy-bootstrap5
```

## Install databases
```
pip3 install dj_database_url==0.5.0 psycopg2
```

## Now to create a django project
The dot makes so we create it in the current directory
```
django-admin startproject daytasker .
```

## Create an application for our project
First we need to direct ourself into the project that we just created.
```
cd daytasker
```
Second we need to create the application
```
python3 manage.py startapp main
```

## Now for our requirements.txt file
```
pip3 freeze --local > requirements.txt
```

## Now to install our app to the project
Within the folder **daytasker** (project) in the **settings.py** add your app.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',  # <<<---- Add your app here >>>
]
```

Now that we added the app to the project we need to **migrate** the database for the new changes that we made.
```
python3 manage.py migrate
```

Test if we done everything correctly.
```
python3 manage.py runserver
```

When opened up the message should be like this:
```
The install worked successfully! Congratulations!
```