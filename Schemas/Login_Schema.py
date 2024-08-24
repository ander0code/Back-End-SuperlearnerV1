from pydantic import BaseModel,EmailStr,field_validator
from fastapi.exceptions import HTTPException


class UserDataSchema(BaseModel):
    id: int
    email: EmailStr
    passwordHash: str

    @field_validator("email")
    def autonoma_email(cls, value):
        if not value.endswith("@superlearnerperu.com"):
            raise HTTPException(
                status_code=400,
                detail="El correo electrónico debe terminar en @superlearnerperu.com"
            )
        return value
    
    class Config:
        from_attributes = True 