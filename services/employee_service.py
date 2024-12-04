from sqlalchemy.orm import Session
from db.employee_db import DBEmployee
from sqlalchemy import func
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

def update_employee(db:Session,employee_id:int,department:str,salary:float):
    """Update an employee's department or salary."""
    employee = db.query(DBEmployee).filter(DBEmployee.id == employee_id).first()
    if not employee:
        return None
    if department:
        employee.department = department
    if salary is not None:
        employee.salary = salary
    db.commit()
    db.refresh(employee)
    return employee
def delete_employee(db: Session, employee_id: int):
    """Delete an employee record."""
    employee = db.query(DBEmployee).filter(DBEmployee.id == employee_id).first()
    if not employee:
        return None
    db.delete(employee)
    db.commit()
    return employee
def filter_employees(db: Session, department: str, min_salary: float, max_salary: float):
    """Filter employees by department or salary range."""
    query = db.query(DBEmployee)

    # Apply filters dynamically
    if department:
        query = query.filter(DBEmployee.department == department)
    if min_salary:
        query = query.filter(DBEmployee.salary >= min_salary)
    if max_salary:
        query = query.filter(DBEmployee.salary <= max_salary)

    # Execute the query
    return query.all()

def calculate_average_salary_by_department(db: Session) -> dict:
    """
    Calculate the average salary for each department.
    """
    # Group by department and calculate the average salary
    results = (
        db.query(DBEmployee.department,func.avg(DBEmployee.salary).label("average_salary"))
        .group_by(DBEmployee.department)
        .all()
    )
    
    # Convert the results into a dictionary
    return {department: round(average_salary, 2) for department, average_salary in results}
