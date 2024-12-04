from pydantic import BaseModel

class Employee(BaseModel):
    id: int # Updated to int for auto-incrementing ID
    name: str
    department: str
    salary: float

    class Config:
        orm_mode = True
        
class NewEmployee(BaseModel):
    name: str
    department: str
    salary: float