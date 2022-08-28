import uvicorn
from typing import Any
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi import Depends,FastAPI,status,HTTPException
from server import models
from server.database import engine,get_db
from server.schema import Record,RecordOut

# create fastapi
# models.Base.create_engine(bind=engine)

app = FastAPI()

#cors middleware to allow requests from all origins 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.include_router(router)

@app.get("/")
def index_route():
     """send request to /results to retrieve the list of results"""
     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Go to url: /results")

@app.get("/results",response_model=list[RecordOut] | list[Any])
def get_results(db: Session = Depends(get_db)):
     """endpoint to return all result instances from database"""
     query = db.query(models.Record).all()
     return query

@app.post("/submit",status_code=status.HTTP_201_CREATED)
def submit_results(rec: Record, db: Session = Depends(get_db)):
     """enpoint to submit results"""
     instance = models.Record(**rec.dict())
     db.add(instance)
     db.commit()
     i = db.refresh(instance)
     return instance