from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

debug = False
if debug == True:
     # to toggle the state of development and productions.
     SQLALCHEMY_DATABASE_URL = "postgresql://postgres:king2002@localhost:5432/result"
else:
     SQLALCHEMY_DATABASE_URL = "postgresql://wssdjzzxksktwj:7acbef1c4e5d544ed4ec45a6a98cb38a9f979972ebcb4e3786ede8bb3d5f6ac0@ec2-3-208-79-113.compute-1.amazonaws.com:5432/d313rbptq5cohj"

engine = create_engine(SQLALCHEMY_DATABASE_URL,)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

def get_db():
     db = SessionLocal()
     try:
          yield db
     finally:
          db.close()