from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:azerty@localhost:5432/testdb'
db = SQLAlchemy(app)



# Use app.app_context() to create a context for your code
with app.app_context():
    # Now you can perform operations that require the application context
    db.create_all()  # Example: Creating database tables


if __name__ == '__main__':
    app.run()