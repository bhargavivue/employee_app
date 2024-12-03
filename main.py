from fastapi import FastAPI
from routers import employees
from db.employee_db import init_db

app = FastAPI()

# Initialize the database (this will create tables)
init_db()

# Include routers
app.include_router(employees.router, prefix="/employees", tags=["Employees"])

@app.get("/")
def root():
    """Root endpoint."""
    return {"message": "Welcome to the Employee Management System!"}
