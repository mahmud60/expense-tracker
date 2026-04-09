from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class ExpenseCreate(BaseModel):
    amount: float = Field(..., gt=0, description="Must be greater than 0")
    category: str = Field(..., min_length=1)
    note: Optional[str] = ""

class ExpenseUpdate(BaseModel):
    amount: Optional[float] = Field(None, gt=0)
    category: Optional[str] = None
    note: Optional[str] = None

class ExpenseResponse(BaseModel):
    id: int
    amount: float
    category: str
    note: str
    date: date
    user_id: int
    
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3)
    password: str = Field(..., min_length=6)

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
