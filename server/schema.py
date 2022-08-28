from pydantic import BaseModel

class Record(BaseModel):
     username: str
     score: str

class RecordOut(BaseModel):
     id: int
     username: str
     score: str
     time_added: str