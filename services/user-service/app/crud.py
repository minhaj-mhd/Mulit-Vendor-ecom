from sqlalchemy.orm import Session
from app import models, schemas
from app.auth import get_password_hash, verify_password

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        email = user.email,
        password_hash = hashed_password,
        first_name = user.first_name,
        last_name = user.last_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return(db_user)
def authenticate_user(db: Session, email:str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user