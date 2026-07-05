from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String)
    address = Column(String)
    devices = relationship("Device", back_populates="customer")

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String, index=True)
    brand =  Column(String, index=True)
    model =  Column(String, index=True)
    problem =  Column(String, index=True)
    customer_id = Column(Integer,ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="devices")
    repairs = relationship("Repair", back_populates="device")


class Repair(Base):
    __tablename__ = "repairs"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    cost =  Column(String, index=True)
    status =  Column(String, index=True)
    received_date =  Column(String, index=True)
    delivered_date = Column(String, index=True)  
    device = relationship("Device", back_populates="repairs")
    device_id = Column(Integer,ForeignKey("devices.id"))
   

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String,default="user")