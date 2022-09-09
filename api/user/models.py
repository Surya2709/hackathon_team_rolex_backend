from sqlalchemy import Column, String, BigInteger, Text, Boolean, DateTime, Enum, Float, JSON
from base.models import BaseModel


class User(BaseModel):
    __tablename__ = 'user_data'

    first_name = Column(String(50), nullable=True)
    middle_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    gender = Column(String(10))
    email = Column(Text)
    dob = Column(DateTime)
    country_code = Column(String(10))
    email_verified =  Column(Boolean())
    password = Column(String(100))
    is_survey_taken = Column(Boolean())

class Address(BaseModel):
    __tablename__ = 'address'

    user_id = Column(String(40))
    city = Column(String(100))
    street = Column(String(100))
    pincode =  Column(String(10))
    country = Column(String(50))
    national_number = Column(String(50))

class TempUser(BaseModel):
    __tablename__ = 'temp_user'

    user_id = Column(String(40))
    device_id = Column(Text)

