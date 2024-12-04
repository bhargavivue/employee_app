from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from services.employee_service import create_employee, get_employee_by_id, list_employees,update_employee,delete_employee,filter_employees,calculate_average_salary_by_department
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
@router.put("/{employee_id}",response_model=Employee)
def get_employee_route(employee_id:int,department:str,
    salary: float,db: Session = Depends(get_db),):
    """Update an employee's department or salary."""
    employee = update_employee(db, employee_id, department, salary)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee
@router.delete("/{employee_id}", response_model=dict)
def delete_employee_route(employee_id: int, db: Session = Depends(get_db)):
    """Delete an employee record."""
    employee = delete_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": f"Employee with ID {employee_id} has been deleted."}

@router.get("/dept/sal-range-emps", response_model=List[Employee])
def filter_employees_route(department:str,min_salary:float,max_salary:float,
    db: Session = Depends(get_db),
):
    """Filter employees by department or salary range."""
    employees = filter_employees(db, department, min_salary, max_salary)
    if not employees:
        raise HTTPException(status_code=404, detail="No employees match the given criteria")
    return employees

@router.get("/depts/avg-sal", response_model=dict)
def get_average_salary_by_department_route(db: Session = Depends(get_db)):
    """
    Calculate and display the average salary of employees grouped by department.
    """
    avg_salaries = calculate_average_salary_by_department(db)
    if not avg_salaries:
        raise HTTPException(status_code=404, detail="No employees found")
    return avg_salaries