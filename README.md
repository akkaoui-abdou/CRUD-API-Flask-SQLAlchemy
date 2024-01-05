# How to build a CRUD API using Python Flask and SQLAlchemy ORM with PostgreSQL


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



Source:

https://pypi.org/project/Flask-SQLAlchemy/
https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/#install-requirements
https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
https://medium.com/@yahiaqous/how-to-build-a-crud-api-using-python-flask-and-sqlalchemy-orm-with-postgresql-7869517f8930
https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_adding_objects.htm
https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/
https://medium.com/@pooya.oladazimi/flask-app-postgres-database-initialization-step-by-step-guide-with-models-7bd251504c3e