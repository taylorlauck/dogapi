from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
 db.app = app
 db.init_app(app)

# MODELS GO BELOW! :)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_made = db.Column(db.Date, nullable=False)
    
    def __init__(self, name, date_made):
        self.name = name
        self.date_made = date_made

class Breed(db.Model):
    __tablename__ = 'breeds'

    id = db.Column(db.Integer, primary_key=True)
    dogs_picked = db.Column(db.String(100), nullable=False)
    
    def __init__(self, dogs_picked):
        self.dogs_picked = dogs_picked

class PickedBreed(db.Model):
    __tablename__ = 'pickedbreeds'

    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    breeds_id = db.Column(db.Integer, db.ForeignKey('breeds.id', ondelete='CASCADE'), nullable=False)
    
    user = db.relationship('User', backref='picked_breeds')
    breed = db.relationship('Breed', backref='picked_breeds')
    
    def __init__(self, users_id, breeds_id):
        self.users_id = users_id
        self.breeds_id = breeds_id
