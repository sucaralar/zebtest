from pydantic import BaseModel


class LoginBase(BaseModel):
    """For get-token existing product(s)"""
    username: str

    class Config:
        orm_mode = True
