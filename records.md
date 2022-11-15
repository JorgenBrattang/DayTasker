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
    'main',  # <<<---- your main app >>>
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
    'main',
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
from django.contrib import admin
from django.urls import path, include
from main import views  # <<< --- Add this >>>

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home'),  # <<< --- Add this >>>
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
                        <a class="nav-link" href="{% url 'account_logout' %}">Logout</a>
                    </li>
                    {% else %}
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'account_signup' %}">Register</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'account_login' %}">Login</a>
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

# Modify the login, register and logout page
First we need to check the python version:
```
ls ../.pip-modules/lib
```

My version is:
```
python3.8
```

Now to modify the pages, we need to copy them into our project:<br>
*(If your python is different, just change where I wrote it to your version. Rest will be the same)*
```
cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates
```

Now you will see more folders within the **templates** folder, navigate to **account** folder and change the following:
```
login.html
logout.html
signup.html
```

On the toprow on all three is this code:
```python
{% extends "account/base.html" %}
```

Change it to our **base.html**:
```python
{% extends "base.html" %}
```

Now as you open your server you can see how it changed to a much better view. We will modify these later, but for now leave it.

# To do application
First lets create the new application:
```
python manage.py startapp tasks
```

This will create a new app, which you need to tell the project to include.<br>
Navigate to **daytasker -> settings.py**:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.staticfiles',
    'main',
    'crispy_forms',
    'crispy_bootstrap5',
    'tasks'  # <<< --- Add this now >>>
]
```

# Now lets make a basic task manager
Navigate to the folder **tasks -> models.py**
```python
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    
    def __str__(self):  # <<< --- This will override the __str__ method so we can view the name >>>
        return self.name
```

And now we need to migrate this to the database to make it official.<br>
First lets do a dry run to make sure we don't mess things up:
```
python3 manage.py makemigrations --dry-run
```
Output
```
Migrations for 'tasks':
  tasks/migrations/0001_initial.py
    - Create model Task
```

Everything looks okey, lets run it without the dry run
```
python3 manage.py makemigrations
```

Now we can run our migration:
```
python3 manage.py migrate
```

To make it showup in the admin panel, navigate to **admin.py** within the **tasks** folder:
```python
from django.contrib import admin
from .models import Task  # <<< --- Add this >>>

admin.site.register(Task)  # <<< --- And this >>>
```

Lets now test it:
```
python3 manage.py runserver
```

And add the **/admin** behind the URL, and there you can now see the **Tasks**

For now we will create two tasks from the **/admin** panel:
```
1. Click on the +Add at the Tasks category
2. Write a name of the task: Im not done
3. Leave the checkbox empty
4. Click on SAVE
```

Repeat:
```
1. Click on the +Add at the Tasks category
2. Write a name of the task: Im done
3. Check the checkbox
4. Click on SAVE
```

Now we got two tasks, one done, and one is not.


# View the task in our website
Navigate to **views.py** within the **tasks** folder:

```python
def get_tasks_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/tasks_list.html', context)
```

This will allow us to render out this in our **html** now, so navigate to **templates -> tasks -> tasks_list.html**:

```html
{% extends 'base.html' %}
{% block title %}Task List{% endblock %}
{% block content %}
    <h1>Tasks List</h1>
    {% for task in tasks %}
        <p>{{ task.name }} is {{ task.done }}</p>
    {% endfor %}
{% endblock %}
```

This is just a test to see how that it is now working, we will add complexity and more to it as we go on.

Now lets test out a if statement:
```html
{% block content %}
    <h1>Tasks List</h1>
    {% for task in tasks %}
        {% if task.done %}
            <p>{{ task.name }} is done</p>
        {% else %}
            <p>{{ task.name }} must be completed</p>
        {% endif %}
    {% endfor %}
{% endblock %}
```

Now we can see our custom view of which task is done, and which is not.

Now lets add if you have nothing to do, the tasks list is empty *(first you need to delete them in the admin panel)*
```
    {% endfor%}
{% empty %}
    <p>Create more tasks, cause you got nothing to do!</p>
{% endfor %}
```

# Create a new task
To let the user create a new task, lets start with adding a link to **tasks_list.html**:<br>
```html
{% endfor %}
<a href="{% url 'add_task' %}">Add Task</a>
{% endblock %}
```

Navigate to **views.py** within the **tasks** folder and add this:
```python
from django.shortcuts import render, redirect  # <<< --- Import redirect >>>

def add_task(request):
    if request.method == 'POST':
        name = request.POST.get('task_name')
        done = 'done' in request.POST
        Task.objects.create(name=name, done=done)
        return redirect('get_tasks_list')
    return render(request, 'tasks/add_task.html')
```

Now to **daytasker -> urls.py**:
```python
from django.contrib import admin
from django.urls import path, include
from tasks.views import get_tasks_list, add_task  # <<< --- Add add_task >>>
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home'),
    path('tasks/', get_tasks_list, name='get_tasks_list'),
    path('add/', add_task, name='add_task')  # <<< --- Add this >>>
]
```

Now create a new html file within the **templates -> tasks** folder called **add_task.html**:
```html
{% extends 'base.html' %}
{% block title %}Task List{% endblock %}
{% block content %}
<h1>Add item</h1>
<form method="POST">
    {% csrf_token %}  <!-- This token is really important to have! --->
    <div>
        <p>
            <label for="id_name">Name: </label>
            <input type="text" id="id_name" name="task_name">
        </p>
    </div>
    <div>
        <p>
            <label for="id_done">Done: </label>
            <input type="checkbox" id="id_done" name="done">
        </p>
    </div>
    <div>
        <p>
            <button type="submit">Add task</button>
        </p>
    </div>
</form>
{% endblock %}
```







# DEBUG enviroment
```
I will say that the setup is a little annoying, because you need to have DEBUG True in your Gitpod workspace, and False in your Heroku workspace.
The way around this is to use an environment variable to make this dynamic:
DEBUG = 'DEVELOPMENT' in os.environ
Then:
add `os.environ['DEVELOPMENT'] = 'Yes!!'
only add 'DEVELOPMENT' to Heroku if you want DEBUG to be enabled
```