#init
from sqlalchemy import Column, String, BigInteger, Text, Boolean, DateTime, Enum, Float, JSON,Integer
from base.models import BaseModel


class Product(BaseModel):
    __tablename__='product'

    name =  Column(String(50),nullable=True)
    description = Column(String(50),nullable=True)
    category_id = Column(String(50),nullable=True)

class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(50),nullable=True)
    description = Column(String(50),nullable=True)

class Sales(BaseModel):
    __tablename__ = 'sales'

    user_id = Column(String(50),nullable=True)
    product_id = Column(String(50),nullable=True)
    market_id = Column(String(50),nullable=True)
    quantity = Column(Float(),nullable=True)
    purchase_value =  Column(Float(),nullable=True)
