from sqlalchemy import Column, String, BigInteger, Text, Integer, ForeignKey
from sqlalchemy.orm import validates

from app.models import BaseModel


class User(BaseModel):
    __tablename__ = 'userdata'

    name = Column(String(20), nullable=True)
    phone_no = Column(BigInteger, nullable=False, unique=True)
    uuid = Column(String(40), default=None)
    otp=Column(String(10), default=None)


class Address(BaseModel):
    __tablename__ = 'address'

    uuid = Column(String(40))
    address = Column(Text)
    landmark = Column(Text)
    save_as = Column(String(10))

