from app.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    profile_picture = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))
    
    
class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    price = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))
    user = relationship("User")
    

class Invoice(Base):
    __tablename__ = "invoice"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=True)
    item_id = Column(Integer,ForeignKey("item.id", ondelete="CASCADE"), nullable=False)
    company_id = Column(Integer,ForeignKey("company.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))
    user = relationship("User")
    
    
    
class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    location = Column(String, nullable=False)
    contact = Column(String, name=True)
    logo = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))
    user = relationship("User")
    
        
    
    
    