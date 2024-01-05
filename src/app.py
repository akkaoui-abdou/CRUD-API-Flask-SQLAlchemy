from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from models import db


#db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:azerty@localhost:5432/testdb'
    db.init_app(app)
    # Use app.app_context() to create a context for your code
    with app.app_context():
        # Now you can perform operations that require the application context
        db.create_all()  # Example: Creating database tables

    # Hello World!
    @app.route('/')
    def hello():
        return "Hello World!"

    # To Run the Server in Terminal => flask run -h localhost -p 5000
    # To Run the Server with Automatic Restart When Changes Occurred => FLASK_DEBUG=1 flask run -h localhost -p 5000
    from urls import bp_user 
    app.register_blueprint(bp_user, url_prefix='/api/')
    
    app.run(debug=True)
    
if __name__ == '__main__':
    create_app()
