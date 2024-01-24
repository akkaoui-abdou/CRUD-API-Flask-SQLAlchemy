# App Initialization
from . import create_app # from __init__ file
import os
app = create_app()

# Hello World!
@app.route('/')
def hello():
 return "Hello World!"

# To Run the Server in Terminal => flask run -h localhost -p 5000
# To Run the Server with Automatic Restart When Changes Occurred => FLASK_DEBUG=1 flask run -h localhost -p 5000
from src.urls import bp_user 
app.register_blueprint(bp_user, url_prefix='/api/')

if __name__ == '__main__':
    app.run(debug=True)
