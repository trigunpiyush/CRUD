# SIMPLE CRUD API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.6
- Django 3.1
- Django REST Framework

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Use

First, we have to start up Django's development server.
```
python manage.py runserver
```
Only authenticated users can use the API services, for that reason if we try this:
```
http  http://127.0.0.1:8000/admin
```
user id - admin
password - spinny@123

user id - staff
password - spinny@123

user id - user
password - spinny@123



### Commands
```
To Create Boxes
http http://127.0.0.1:8000/boxes/create/ 
Update dimensions of a box with a given id
http PUT  http://127.0.0.1:8000/boxes/update/int:id/  'provide integer at "int:id" '
eg. -  http://127.0.0.1:8000/boxes/update/1/
List Of All Boxes
http GET http://127.0.0.1:8000/boxes/list/ 
List my boxes
http PATCH http://127.0.0.1:8000/api/my_boxes/ 
Delete a box with a given id:
http DELETE http://127.0.0.1:8000/boxes/delete/int:id/  'provide integer at "int:id" '
eg. -  http://127.0.0.1:8000/boxes/delete/1/
```

```

