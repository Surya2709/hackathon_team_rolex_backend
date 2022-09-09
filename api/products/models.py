
#init
import string
from sqlalchemy import Column, String, BigInteger, Text, Boolean, DateTime, Enum, Float, JSON,Integer, Time
from base.models import BaseModel




class ProductMarketMapping(BaseModel):
    __tablename__ = 'product_market_mapping'

    product_id = Column(String(50),nullable=True)
    market_id = Column(String(50),nullable=True)
    avg_price = Column(Integer(),nullable=True)
    last_sold_price = Column(Float(),nullable=True)
