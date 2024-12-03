from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from services.employee_service import create_employee, get_employee_by_id, list_employees
from models.employee import Employee, NewEmployee
from db.employee_db import get_db

# Create router
router = APIRouter()

@router.post("/", response_model=Employee)
def create_employee_route(employee: NewEmployee, db: Session = Depends(get_db)):
    """Create a new employee with an auto-generated ID."""
    return create_employee(db, employee.name, employee.department, employee.salary)

@router.get("/", response_model=List[Employee])
def get_all_employees_route(db: Session = Depends(get_db)):
    """Get all employees."""
    return list_employees(db)

@router.get("/{employee_id}", response_model=Employee)
def get_employee_route(employee_id: int, db: Session = Depends(get_db)):
    """Get an employee by their ID."""
    employee = get_employee_by_id(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee
