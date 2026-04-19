from pydantic import BaseModel, EmailStr, Field

# Base schema (shared fields)
class UserBase(BaseModel):
    email: EmailStr

# Request schema for registration
class UserCreate(UserBase):
    password: str = Field(min_length=6)

# Request schema for login
class UserLogin(UserBase):
    password: str

# Response schema (what we send back)
class UserResponse(UserBase):
    id: str

    class Config:
        from_attributes = True