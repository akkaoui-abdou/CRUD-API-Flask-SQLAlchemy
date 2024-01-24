
 # encoding: utf-8
from sqlalchemy import ForeignKeyConstraint, DateTime, inspect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    role = db.Column(db.String(), default="employee")    


    def __init__(self, username, password, email):
        self.username = username        
        self.password = password        
        self.email = email
    

    def register_user_if_not_exist(self):        
        db_user = User.query.filter(User.username == self.username).all()
        if not db_user:
            db.session.add(self)
            db.session.commit()
        
        return True
    

    def get_by_username(username):        
        db_user = User.query.filter(User.username == username).first()
        return db_user

    # How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return '<User %r>' % self.username






class Car(db.Model):

    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)     
    model = db.Column(db.String(), nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)    

    
    __table_args__ = (        
        ForeignKeyConstraint([owner_id], [User.id], ondelete='NO ACTION'),        
    )

    

    def __init__(self, model, owner_id):
        self.model = model
        self.owner_id = owner_id      
    
    """
    def to_dict(self):
        return {
            'model': self.model,
            'owner': self.owner_id            
        }
    """
    # How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }


    def buy_car(self):
        record = Car.query.filter(Car.id == self.id).first()
        if not record:
            db.session.add(self)
            db.session.commit()
        
        return True



    def get_user_cars(user_id):
        records = Car.query.filter(Car.owner_id == user_id).all()
        return [record.to_dict() for record in records] 



    def __repr__(self):
        return f"<Car {self.model}>"