from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import session
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas import User, UserCreate
from app import crud, auth, dependencies, events
from app.database import Base, engine
from app.config import Settings

Base.metadata.create_all(bind = engine)
app = FastAPI(title="User Service")

@app.post("/users/register",response_model=User)
def register_user(user:UserCreate, db: session = Depends(dependencies.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already Registered!")
    new_user = crud.create_user(db=db,user=user)
    events.publish_event("user_events", {"type":"user_registered", "user_id": str(new_user.user_id)})
    return new_user

