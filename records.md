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

## Now to install our apps to the project
Within the folder **daytasker** (project) in the **settings.py** add your app.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',  # <<<---- your main app >>>
    'crispy_forms',  # <<<---- Crispy_forms (for later use) >>>
    'crispy_bootstrap5'  # <<<---- And Crispy bootstrap >>>
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

Also add to the **Config Vars**:
```
KEY: PORT
VALUE: 8000
```

For now we will also add this:
```
KEY: DISABLE_COLLECTSTATIC
VALUE: 1
```
This is because we don't have any **HTML** connected yet. So this will be take away when we are building up the views.

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

## Static and templates
Lets add some line of code for the static folder
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

Now lets create a TEMPLATES_DIR for our templates:
```python
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
```

Change the **DIRS** to **[TEMPLATES_DIR]**

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR], # This one was empty before
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Now lets add **ALLOWED_HOSTS**
```python
ALLOWED_HOSTS = ['daytasker.herokuapp.com', 'localhost']
```

## Now for the folders and some files that we need later on.
- First create a called **templates** in the outer location so not inside **daytasker** or **main** folder. *(spelling here is crucial)*. 
- Create a new folder called **main**.
- In there create two files:
    - **base.html**
    - **home.html**
- Also create a **static** folder at the same place as **templates** *(again, spelling is cruicial)*

## The Procfile for Heroku
Create a new file called **Procfile**, where the file **manage.py** is.
You can use this in the terminal
```
touch Procfile
```
And that will create a Procfile for you.

We need this file to run our project.
Write this code within that file:
```
web: gunicorn daytasker.wsgi
```
*(daytasker is the projectname)*

# Back to Heroku
- Navigate back to **Heroku** to the **Deploy** tab
- Deployment method -> **GitHub - Connect to GitHub**
- Select your repository -> Search for your **repo-name** which in this case is **daytasker**
- Press on the button **Connect**
- Go down and press on **Deploy Branch**

After that is complete, if you followed the steps you should see this beautiful message!
```
Your app was successfully deployed.
```

# Admin creation
First we need to create a superuser for our project:
```
python3 manage.py createsuperuser
```

Here you are promted to add a username:
```
Username (leave blank to use 'gitpod'): 
```

So Im just going to use **admin**

Next is an email adress:
```
Email Adress:
```

Then a password, which you can't see as your writing it:
```
Password: 
```
```
Password (again): 
```
```
Superuser created successfully.
```

To access the **admin page** open up the server:
```
python3 manage.py runserver
```

And put this at the end of the **URL**
```
/admin

example: https://...gitpod.io/admin
```

Now lets add more functionality to our registration by installing **django-allauth**
<a>https://django-allauth.readthedocs.io/en/latest/</a>

```
pip3 install django-allauth
```

Onces installed, freeze the requirements too:
```
pip3 freeze --local > requirements.txt
```

Now navigate to **daytasker -> urls.py**:
```python
from django.urls import path, include  # <<< --- Add include here >>>

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # <<< --- And add this>>>
]
```

Then we need to add it to our **settings.py** file:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',  # <<< --- This >>>
    'allauth',  # <<< --- And this >>>
    'allauth.account',  # <<< --- And that >>>
    'allauth.socialaccount',  # <<< --- And finally this one >>>
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'crispy_forms',
    'crispy_bootstrap5'
]
```

Also we need this to make it work, and this will go under **INSTALLED_APPS**:
```python
SITE_ID = 1  # <<< --- You need to add this for Django, it likes it. >>>

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_EMAIL_VERIFICATION = 'none'  # <<< --- This one is for so you don't need email to create an account >>>
```

Now to implement this, we need to **migrate**:
```
python3 manage.py migrate
```

# Now lets make so we can view it all
Start with going to **daytasker -> urls.py**
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('main.urls')),  # <<< --- Add this >>>
]
```

Create a new file in **main** called **urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')
]
```

Now navigate to **views.py** within the **main** folder:
```python
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
```

# Add the HTML thats needed
Navigate to **templates -> base.html**:
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <title>{% block title %}{% endblock %}</title>
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <div>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="/home">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/create-task">Task</a>
                    </li>
                </ul>
            </div>
            <div>
                <ul class="navbar-nav">
                    {% if user.is_authenticated %}
                    <li class="nav-item">
                        <a class="nav-link" href="accounts/logout">Logout</a>
                    </li>
                    {% else %}
                    <li class="nav-item">
                        <a class="nav-link" href="accounts/sign-up">Register</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="accounts/login">Login</a>
                    </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>
    <div class="container">
        {% block content %}
        {% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous">
    </script>
</body>
</html>
```

And now to **home.html**
```html
{% extends 'base.html' %}
{% block title %}Home page{% endblock %}
{% block content %}
<h1>Home page</h1>
{% endblock %}
```

For the test go start the server if you don't have it running:
```
python3 manage.py runserver
```

Test the these links if they work:
```
Register
Login
Logout
```
If it all works, then great! Otherwise go back and check where you might have gone wrong.