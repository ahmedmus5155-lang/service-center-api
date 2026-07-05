from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

import models
import crud
import schemas
from database import get_db, engine
from security import create_access_token
from security import get_current_user
from security import require_admin
from fastapi.security import OAuth2PasswordRequestForm


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "welcome to service center API"}
    
@app.post("/customer")
def create_customer(
    customer: schemas.CustomerCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.create_customer(db, customer)

@app.get('/customers')
def get_customers(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.get_customers(db)

@app.get('/customers/{customer_id}')
def get_customer(
    customer_id:int,db:Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)

):
    customer = crud.get_customer(db,customer_id)
    if customer is None:
        raise HTTPException(
        status_code=404, 
        detail='customer not found'
    )
    return customer

@app.put('/customers/{customer_id}')
def update_customer(
    customer_id:int,customer:schemas.CustomerUpdate,db:Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    
    update_customer = crud.update_customer(db,customer_id,customer)
    
    if update_customer is None:
        raise HTTPException(
        status_code=404, 
        detail='customer not found'
     )    
    return update_customer    

@app.delete('/customers/{customer_id}')
def delete_customer(
    
    customer_id:int,db:Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    deleted_customer = crud.delete_customer(db, customer_id)

    if deleted_customer is None:
        raise HTTPException(
        status_code=404,
        detail="Customer not found"
    )

    return deleted_customer



@app.post('/devices')
def create_device(
    device: schemas.DeviceCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):    
    return crud.create_device(db,device)

@app.get('/devices')
def get_devices(
    db:Session = Depends(get_db)

):
    return crud.get_devices(db,) 

@app.get('/devices/{device_id}')
def get_device(
    device_id:int,db:Session = Depends(get_db),
     current_user: models.User = Depends(get_current_user)
):
    device = crud.get_device(db,device_id)
    if device is None:
        raise HTTPException(
        status_code=404, 
        detail='device not found'
    )
    return device

@app.put('/devices/{device_id}')
def update_device(
    device_id:int,device:schemas.DeviceUpdate,db:Session = Depends(get_db),
     current_user: models.User = Depends(get_current_user)
):

    
    update_device = crud.update_device(db,device_id,device)
    
    if update_device is None:
        raise HTTPException(
        status_code=404, 
        detail='device not found'
     )    
    return update_device    

@app.delete('/devices/{device_id}')
def delete_device(
    
    device_id:int,db:Session = Depends(get_db),
     current_user: models.User = Depends(require_admin)
):

    deleted_device = crud.delete_device(db, device_id)

    if deleted_device is None:
        raise HTTPException(
        status_code=404,
        detail="device not found"
    )

    return deleted_device





@app.post('/repairs')
def create_repair(
    repair:schemas.RepairCreate,db:Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)

):    
    return crud.create_repair(db,repair)

@app.get('/repair')
def get_repair(
    db:Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
    

):
    return crud.get_repair(db,) 

@app.get('/repairs/{repair_id}')
def get_repair(
    repair_id:int,db:Session = Depends(get_db)
):
    repair = crud.get_repair(db,repair_id)
    if repair is None:
        raise HTTPException(
        status_code=404, 
        detail='repair not found'
    )
    return repair

@app.put('/repairs/{repair_id}')
def update_repair(
    repair_id:int,repair:schemas.RepairUpdate,db:Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    
    update_repair = crud.update_repair(db,repair_id,repair)
    
    if update_repair is None:
        raise HTTPException(
        status_code=404, 
        detail='repair not found'
     )    
    return update_repair    

@app.delete('/repairs/{repair_id}')
def delete_repair(
    
    repair_id:int,db:Session = Depends(get_db),
     current_user: models.User = Depends(require_admin)
):

    deleted_repair = crud.delete_repair(db, repair_id)

    if deleted_repair is None:
        raise HTTPException(
        status_code=404,
        detail="repair not found"
    )

    return deleted_repair

@app.post("/register")
def register(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = crud.get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return crud.create_user(db, user)


@app.post("/login")
def login(
    login: schemas.UserLogin,
    db: Session = Depends(get_db)
):
    user = crud.login_user(db, login)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={"sub": user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
