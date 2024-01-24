# How to build a CRUD API using Python Flask and SQLAlchemy ORM with PostgreSQL


### In this tutorial, you will learn how to build a simple CRUD API using Flask, SQLAlchemy, and PostgreSQL.

![alt text](https://github.com/akkaoui-abdou/CRUD-API-Flask-SQLAlchemy/images/Flask-SQLAlchemi-PosgreSQL.png)

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

    $ source bin/activate


# Install the Project Dependencies

    pip install -U Flask-SQLAlchemy psycopg2-binary

# create a requirements file using this command:

    pip freeze > requirements.txt

# Using env variable

    import os
    from dotenv import load_dotenv

    load_dotenv()

    GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')
    SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
    STORAGE_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME')



# Instegrate JWTManager

### Install package 

    pip install flask-jwt-extended

# Run flask
    flask run -h 127.0.0.2 -p 5001


# Migrate the new database models with these commands:

    flask db init
    flask db migrate
    flask db upgrade



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