from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str

class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseSchema(BaseModel):
    user: UserSchema