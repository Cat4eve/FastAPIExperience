from pydantic import BaseModel

class Employee(BaseModel):
    first_last_name: str
    age: int
    position: str
    remote: bool
    id: str | None

class RawEmployee(BaseModel):
    first_last_Name: str
    age: int
    position: str
    remote: bool
    photo: bytes