from .database import Base
from sqlalchemy import Column,String,Integer
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text



class Record(Base):
     __tablename__ = "record"
     id = Column(Integer,primary_key=True)
     username = Column(String,nullable=False)
     score = Column(String,nullable=False)
     date_added = Column(TIMESTAMP(timezone=True),server_default=text("now()"),nullable=False)
