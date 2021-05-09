from app.models import BaseModel
from sqlalchemy import Column, String, BigInteger, Text, Integer, ForeignKey

class User(BaseModel):
    __tablename__ ='user'
    emp_id=Column(String(20))
    password=Column(String(40))
    company_id=Column(String(10))
    first_name = Column(String(20))
    last_name=Column(String(20))
    role=Column(String(30))
    team=Column(String(30))
    domain=Column(String(30))
    detail_designation=Column(String(40))
    type=Column(String(30))
    contract=Column(String(10))
    phone_no=Column(String(10))
    status=Column(String(10))