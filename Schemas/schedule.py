from pydantic import BaseModel
from typing import List,Optional

class data_schedule(BaseModel):
    
    day : str
    init_time : str
    end_time : str

class data_course(BaseModel):
    
    id : int
    name : str 
    schedule : List[Optional[data_schedule]]= None
    







