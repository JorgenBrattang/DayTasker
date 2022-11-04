# Walk-through to how I built my Website.
*(This will not cover everything, like every detail within the HTML and CSS)*
First we need to install a few things to start the project.

# First steps

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

# Heroku
Navigate to the Heroku website
<a>https://id.heroku.com/login</a>
- Login to your account.
- Press on **New** *(up in the right corner)* -> **Create new app**
- App name: **daytasker** *(This is what I used, can't be used again!)*
- Choose Region: **Europe** *(Again, this is what I used)*
- Create App
- Navigate to **Resources**
- Add ons -> Search for **Postgres**
- Select **Heroku Postgres**
- Plan name: **Hobby-dev Free** -> Submit Order Form
- Navigate to **Settings**
- **Config Vars** -> **Reveal Config Vars**
- Copy the **DATABASE_URL** path, starts with: **postgres://...**

## Create env.py file
Now lets create a new file called **env.py** to store our data thats needed for our enviroment such as passwords etc..
This needs to be placed in the same place as **manage.py** file.

***Important!*** - Make sure the env.py is included in the .gitignore file!

Then write this code:
```python
import os

os.environ["DATABASE_URL"] = "postgres://..."
os.environ["SECRET_KEY"] = "superScretKey!!"
```
***For security purpose i will not add mine here. Just replace it with yours.***<br>
*I got my secret key from this generator:<br>*
<a>https://miniwebtool.com/django-secret-key-generator/</a>

Navigate to **Heroku** again and within the **Config Vars** add the values:<br>
```
KEY: SECRET_KEY
VALUE: superScretKey!!
```

## Setup the settings.py file
Navigate to the **settings.py** file within the **daytasker** folder.
Write this code:
```python
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env
```

Change the **SECRET_KEY** to the os enviroment instead that is in the **env.py** file:
```python
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
```

Now for the **DATABASES**:
```python
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```

Now lets run the migrate command again, to implement the changes we made:
```
python3 manage.py migrate
```