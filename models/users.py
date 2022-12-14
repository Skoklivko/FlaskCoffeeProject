from db import db
from models.enums import UserRole


class BaseUserModel(db.model):
    __abstract__ = True 

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(14), nullable=False)
    password = db.Column(db.String(255), nullable=False)


class CustomerModel(BaseUserModel):
    __tablename__ = 'customer'

    orders = db.relationship("OrderModel", backref="order", lazy='dynamic')
    role = db.Column(db.Enum(UserRole), default=UserRole.customer, nullable=False)


class AdminModel(BaseUserModel):
    __tablename__ = 'admin'
    role = db.Column(db.Enum(UserRole), default=UserRole.admin, nullable=False)