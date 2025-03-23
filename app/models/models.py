from app import db
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_name = db.Column(db.String(30), unique=True, nullable=False)
    phone_number = db.Column(db.String(10), nullable=False, default='0000000000')
    email_id = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(10), nullable=False, default='user')

class SampleMenu(db.Model):
    __tablename__ = 'sample_menu'
    id = db.Column(db.Integer, primary_key=True)
    food_items = db.Column(db.String(30), nullable=False)
    is_veg = db.Column(db.Boolean, nullable=False, default=False)
    price = db.Column(db.Float, nullable=False, default=0.0)
