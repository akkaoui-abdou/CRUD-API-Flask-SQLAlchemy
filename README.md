# How to build a CRUD API using Python Flask and SQLAlchemy ORM with PostgreSQL


### In this tutorial, you will learn how to build a simple CRUD API using Flask, SQLAlchemy, and PostgreSQL.

![alt text](https://github.com/akkaoui-abdou/CRUD-API-Flask-SQLAlchemy/blob/main/imges/Flask-SQLAlchemi-PosgreSQL.png)

# Create PostgreSQL Database

### Terminal, Run the PostgreSQL Server

    ~ sudo service postgresql start
    ➜ * Starting PostgreSQL 14 database server
    # 14 is the PostgreSQL Server Version

### Activate the PostgreSQL Shell

    ~ sudo -u postgres psql
    ➜ postgres=#

### Create a New Database

    <!-- create database DBNAME; -->
    postgres=# create database testdb;
    ➜ CREATE DATABASE

### Create a Database User, then Grant Privileges to it

    <!-- create user USERNAME with encrypted password 'PASSWORD'; -->
    postgres=# create user testuser with encrypted password 'testpass';
    ➜ CREATE ROLE

    <!-- grant all privileges on database DBNAME to USERNAME; -->
    postgres=# grant all privileges on database testdb to testuser;
    ➜ GRANT

### Exit the Shell

    postgres=# \q


### Connect to the New Database

    ~ psql -U testuser -h 127.0.0.1 -d testdb
    Password for user testuser: testpass
    ➜ testdb=>


### Check the Connection

    testdb=> \conninfo
    ➜ You are connected to database "testdb" as user "testuser" on host "127.0.0.1" at port "5432".
    <!-- We need this information later for the env file -->


# Initialize the Virtual Environment

    $ python3 -m venv env

# Activate Virtual Environment

    $ source env/bin/activate


# Install the Project Dependencies

    pip install -U flask Flask-SQLAlchemy psycopg2-binary Flask-JWT-Extended python-dotenv Flask-Migrate

# create a requirements file using this command:

    pip freeze > requirements.txt


# Writing the Project Code

        └── src
            ├── app.py
            ├── config.py
            ├── controllers.py
            ├── __init__.py
            ├── models.py
            └── urls.py


# Run flask

    flask run -h 127.0.0.2 -p 5001


# Migrate the new database models with these commands:

    flask db init
    flask db migrate
    flask db upgrade

# Send Requests Using Postman

### 1. Post new User:

- Request Method: POST
- Request Link: http://127.0.0.2:5001/api/user
- Body Data in form-data:

{
    "username":"akkaoui",
    "password":"OLEm#-!",
    "email":"email@gmail.com"
}

![alt text](https://github.com/akkaoui-abdou/CRUD-API-Flask-SQLAlchemy/blob/main/imges/register_user.png)


### 2. List All Users:

- Request Method: GET
- Request Link: http://127.0.0.2:5001/api/user


![alt text](https://github.com/akkaoui-abdou/CRUD-API-Flask-SQLAlchemy/blob/main/imges/CreateNewUser.png)


Source:

https://pypi.org/project/Flask-SQLAlchemy/
https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/#install-requirements
https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
https://medium.com/@yahiaqous/how-to-build-a-crud-api-using-python-flask-and-sqlalchemy-orm-with-postgresql-7869517f8930
https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_adding_objects.htm
https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/
https://medium.com/@pooya.oladazimi/flask-app-postgres-database-initialization-step-by-step-guide-with-models-7bd251504c3e


### Implement a simple JWT with Flask

https://4geeks.com/lesson/what-is-JWT-and-how-to-implement-with-Flask

https://ankushkunwar7777.medium.com/flask-jwt-extended-explanation-aa7b8660c8bb

https://github.com/vimalloc/flask-jwt-extended/blob/master/examples/simple.py


## Repo Flask and SQLAlchemi

https://github.com/Pooya-Oladazimi/flask-cool-app

## Test

https://stackoverflow.com/questions/75523569/runtimeerror-a-sqlalchemy-instance-has-already-been-registered-on-this-flask

## Commands PosgreSQL

https://stackoverflow.com/questions/769683/how-to-show-tables-in-postgresql