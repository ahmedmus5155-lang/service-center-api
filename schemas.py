from pydantic import BaseModel, ConfigDict
from pydantic import BaseModel,EmailStr,Field

class CustomerCreate(BaseModel):
    name:str
    phone:str 
    address:str
        

class CustomerUpdate(BaseModel):
    name:str
    phone:str 
    address:str


class CustomerResponse(BaseModel):
    id: int
    name: str
    phone: str
    address: str

    model_config = ConfigDict(from_attributes=True)

class DeviceCreate(BaseModel):
    device_name:str
    brand:str
    model:str
    problem:str
    customer_id:int

    

class DeviceUpdate(BaseModel):
    device_name:str
    brand:str
    model:str
    problem:str
    customer_id:int


class DeviceResponse(BaseModel):
    id:int
    device_name:str
    brand:str
    model:str
    problem:str
    customer_id:int

model_config = ConfigDict(from_attributes=True)


class RepairCreate(BaseModel):
    description:str
    cost:str
    status:str
    received_date:str
    delivered_date:str
    device_id:int

    

class RepairUpdate(BaseModel):
    description:str
    cost:str
    status:str
    received_date:str
    delivered_date:str
    device_id:int


class RepairResponse(BaseModel):
    id:int
    description:str
    cost:str
    status:str
    received_date:str
    delivered_date:str
    device_id:int

model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(min_length=8, max_length=50)
    role: str = "user"


class UserUbdate(BaseModel):
    username:str
    email:str    

class UserResponse(BaseModel):
    id:int
    username:str
    password:str

    class config:
        from_attributes = True 

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=50)