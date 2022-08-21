from sqlalchemy import func
from db import db 
from models.enums import OrderState


class OrderModel(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, server_default=func.now())
    status = db.Column(db.Enum(OrderState), nullable=False, default=OrderState.pending)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    customer = db.relationship("OrderModel")