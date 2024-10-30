from sqlalchemy import create_engine, Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for models
Base = declarative_base()

# Define the Contract model
class Contract(Base):
    __tablename__ = 'contracts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False)
    expiry_date = Column(Date, nullable=False)
    department = Column(String(50), nullable=False)
    part_number = Column(String(20), nullable=False)
    part_description = Column(Text, nullable=True)
    reason = Column(Text, nullable=True)

# SQLite or PostgreSQL connection
DATABASE_URL = "sqlite:///contracts.db"  # Change this if using PostgreSQL

# Create engine and session
engine = create_engine(DATABASE_URL, echo=True)  # Set echo=True for SQL logging
Session = sessionmaker(bind=engine)
session = Session()

# Create the contracts table in the database (if it doesn't exist)
Base.metadata.create_all(engine)