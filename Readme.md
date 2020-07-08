# activity tracker
# Project Setup
The project backend has been implmented using Django-Rest-Framework and database used is RDBMS (SQLite).
Steps to setup the project on your machine- 
1) Create a virtual environment using command 
>         virtualenv venv -p python3
2) Activate virtual environment using command 
>         source venv/bin/activate
3) Install requirements using command
>         pip install -r requirements.txt
4) Now make migrations for activity app using commands - 
>         python manage.py makemigrations activity
>         python manage.py migrate activity
5) To populate the database with dummy data run the following custom managenment comand -
>         python manage.py populate_dummy_data
6) Run Django server using command
>         python manage.py runserver
All set !!

# List of APIs and their functionalities
API | Request Body | Method | Description | Response
|---|---|---|---|---|
| [/activity/users/] | param - "format=json" | GET | list all the users along with their active periods | json containing users along with their active periods

# Pythonanywherelink -
http://tanaysaxena97.pythonanywhere.com/activity/users/?format=json
