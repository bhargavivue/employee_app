from sqlalchemy import Integer, create_engine, Column, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Setup SQLite database connection
DATABASE_URL = "sqlite:///./test.db"  # Local SQLite file

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

class DBEmployee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String)
    department = Column(String)
    salary = Column(Float)

# Initialize the database
def init_db():
    Base.metadata.create_all(bind=engine)

# Create a new session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
