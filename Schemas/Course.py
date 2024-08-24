from pydantic import BaseModel
from datetime import datetime

class data(BaseModel):
    
    id : int
    category : str
    name : str
    status : bool
    created_at : datetime
    updated_at : datetime
    
    class Config:
        from_attributes = True 

