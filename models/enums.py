from enum import Enum


class UserRole:
    customer = "Customer"
    admin = "Admin"


class OrderState(Enum):
    pending = "pending"
    approved = "approved"
    shipped = "shipped"