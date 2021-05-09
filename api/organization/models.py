from app.models import BaseModel
from sqlalchemy import Column, String, BigInteger, Text, Integer, ForeignKey


class Organization(BaseModel):
    __tablename__='organization'
    company_code=Column(String(20),primary_key=True)
    name=Column(String(100))
    display_name=Column(String(40))
    default_password=Column(String(30))
    address=Column(String(100))
    state=Column(String(20))
    city=Column(String(30))
    pincode=Column(String(10))
    email=Column(String(50))



