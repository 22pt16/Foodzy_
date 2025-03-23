from app import db  
from uuid import uuid4
from datetime import datetime



# Sample Menu Model
class SampleMenu(db.Model):
    __tablename__ = 'sample_menu'
    id = db.Column(db.Integer, primary_key=True)
    food_items = db.Column(db.String(30), nullable=False)
    is_breakfast = db.Column(db.Boolean, default=False)
    is_lunch = db.Column(db.Boolean, default=False)
    is_dinner = db.Column(db.Boolean, default=False)
    is_veg = db.Column(db.Boolean, nullable=False, default=False)
    description = db.Column(db.String(150), nullable=False, default='Delicious food item')
    price = db.Column(db.Float, nullable=False, default=0)
    picture = db.Column(db.String, nullable=False, default='img/menu-1.png')
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)

# Users Model
class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    user_name = db.Column(db.String(30), nullable=False, unique=True)
    phone_number = db.Column(db.String(10), nullable=False, default='0000000000')
    email_id = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(10), nullable=False, default='user')
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)

# Cart Model
class Cart(db.Model):
    __tablename__ = 'cart'
    cart_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('users.user_id'), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('sample_menu.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    price = db.Column(db.Float, nullable=False, default=0)
    date = db.Column(db.Date, default=datetime.utcnow().date())
    time = db.Column(db.Time, default=datetime.utcnow().time())

# Bill Model
class Bill(db.Model):
    __tablename__ = 'bill'
    bill_number = db.Column(db.String(8), primary_key=True)
    cart_id = db.Column(db.String(36), db.ForeignKey('cart.cart_id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.user_id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False, default=0)
    date = db.Column(db.Date, default=datetime.utcnow().date())
    by_user = db.Column(db.String(30), db.ForeignKey('users.user_name'), nullable=False)

# Feedback Model
class Feedback(db.Model):
    __tablename__ = 'feedback'
    user_name = db.Column(db.String(30), nullable=False)
    email_id = db.Column(db.String(50), primary_key=True)
    profession = db.Column(db.String(50))
    messages = db.Column(db.String(150))
    picture = db.Column(db.String, nullable=False, default='img/user.png')
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
