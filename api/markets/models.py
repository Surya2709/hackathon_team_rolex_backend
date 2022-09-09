
from sqlalchemy import Column, String, BigInteger, Text, Boolean, DateTime, Enum, Float, JSON,Integer
from base.models import BaseModel


class Market(BaseModel):
    __tablename__ = "market"

    name = Column(String(50),nullable=True)
    area = Column(String(50),nullable=True)
    city = Column(String(50),nullable=True)
    state = Column(String(50),nullable=True)
    latitude = Column(String(50),nullable=True)
    longitude = Column(String(50))
    open_time = Column(DateTime(),nullable=True)
    close_time = Column(DateTime(),nullable=True)
    is_open = Column(Boolean(),nullable=True)



class Warehouses(BaseModel):
    __tablename__ = 'warehouses'

    name = Column(String(50),nullable=True)
    area = Column(String(50),nullable=True)
    city = Column(String(50),nullable=True)
    state = Column(String(50),nullable=True)
    longitude = Column(String( 50))
    latitude = Column(String(50),nullable=True)
    open_time = Column(DateTime(),nullable=True)
    close_time = Column(DateTime(),nullable=True)
    is_open = Column(Boolean(),nullable=True)

class Product_Market_Mapping(BaseModel):
    __tablename__ = 'product_market_mapping'
    product_id = Column(String(50), nullable=True)
    market_id = Column(String(50), nullable=True)
    avg_price = Column(String(50), nullable=True)
    last_sold_price = Column(String(50))
