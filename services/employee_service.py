from sqlalchemy.orm import Session
from db.employee_db import DBEmployee


# Service Layer: Contains business logic

def create_employee(db: Session, name: str, department: str, salary: float):
    """Create a new employee in the database."""
    #employee_id = generate_employee_id()  # Generate unique ID
    new_employee = DBEmployee(name=name, department=department, salary=salary)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def get_employee_by_id(db: Session, employee_id: int):
    """Retrieve an employee by their ID."""
    return db.query(DBEmployee).filter(DBEmployee.id == employee_id).first()

def list_employees(db: Session):
    """List all employees."""
    return db.query(DBEmployee).all()
