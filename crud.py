from sqlalchemy.orm import Session
import models
import schemas
from security import hash_password, verify_password

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(
        name=customer.name,
        phone=customer.phone,
        address=customer.address
    )

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def get_customers(db: Session):
    return db.query(models.Customer).all()

def get_customer(db: Session,customer_id:int):
    return db.query(models.Customer).filter(
    models.Customer.id == customer_id
).first() 

def update_customer(
    db: Session,
    customer_id: int,
    customer_update: schemas.CustomerUpdate
):
    db_customer = db.query(models.Customer).filter(
        models.Customer.id == customer_id
    ).first()

    if db_customer is None:
        return None

    db_customer.name = customer_update.name
    db_customer.phone = customer_update.phone
    db_customer.address = customer_update.address

    db.commit()
    db.refresh(db_customer)

    return db_customer


def delete_customer(db: Session, customer_id: int):
    db_customer = db.query(models.Customer).filter(
        models.Customer.id == customer_id
    ).first()

    if db_customer is None:
        return None

    db.delete(db_customer)

    db.commit()
    
    return db_customer



    
def create_device(db: Session, device: schemas.DeviceCreate):
    db_device = models.Device(
        device_name=device.device_name,
        brand=device.brand,
        model=device.model,
        problem=device.problem,
        customer_id=device.customer_id
    )

    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device


def get_devices(db: Session):
    return db.query(models.Device).all()

def get_device(db: Session,device_id:int):
    return db.query(models.Device).filter(
    models.Device.id == device_id
).first() 



def update_device(db: Session, device_id: int, device_update:schemas.DeviceUpdate):
    db_device = db.query(models.Device).filter(
        models.Device.id == device_id
    ).first()

    if db_device is None:
        return None

    db_device.device_name = device_update.device_name
    db_device.brand = device_update.brand
    db_device.model = device_update.model
    db_device.problem = device_update.problem
    db_device.customer_id = device_update.customer_id

    db.commit()
    db.refresh(db_device)

    return db_device


def delete_device(db: Session, device_id: int):
    db_device = db.query(models.Device).filter(
        models.Device.id == device_id
    ).first()

    if db_device is None:
        return None

    db.delete(db_device)

    db.commit()
    
    return db_device




    
def create_repair(db: Session, repair: schemas.RepairCreate):
    db_repair = status.Repair(
        description=repair. description,
        cost=repair.cost,
        status=repair.model,
        received_date=repair.received_date,
        delivered_date=repair.delivered_date,
        device_id=repair.device_id
    )

    db.add(db_repair)
    db.commit()
    db.refresh(db_repair)
    return db_repair


def get_repairs(db: Session):
    return db.query(status.Repair).all()

def get_repair(db: Session,repair_id:int):
    return db.query(status.Repair).filter(
    status.Repair.id == repair_id
).first() 



def update_repair(db: Session, repair_id: int, repair_update:schemas.RepairUpdate):
    db_repair = db.query(status.Repair).filter(
        status.Repair.id == repair_id
    ).first()

    if db_repair is None:
        return None
        
    db_repair.description = repair_update.description
    db_repair.cost = repair_update.cost
    db_repair.status = repair_update.status
    db_repair.received_date = repair_update.received_date
    db_repair.delivered_date = repair_update.delivered_date
    db_repair.device_id = repair_update.device_id

    db.commit()
    db.refresh(db_repair)

    return db_repair


def delete_repair(db: Session, repair_id: int):
    db_repair = db.query(status.Repair).filter(
        status.Repair.id == repair_id
    ).first()

    if db_repair is None:
        return None

    db.delete(db_repair)

    db.commit()
    
    return db_repair

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
        role=user.role
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(
        models.User.email == email
    ).first()


def login_user(db: Session, login: schemas.UserLogin):
    user = get_user_by_email(db, login.email)

    if user is None:
        return None

    if not verify_password(
        login.password,
        user.hashed_password
    ):
        return None

    return user