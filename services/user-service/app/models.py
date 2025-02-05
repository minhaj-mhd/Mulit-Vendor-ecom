from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True),primary_key=True, default=uuid.uuid4)
    email = Column(String, unique= True , index= True, nullable= False)
    password_hash = Column(String,nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    date_joined = Column(DateTime,default = datetime.utcnow)
    last_login = Column(DateTime)
    role = Column(Enum("customer","admin",name="user_roles"),default="customer")