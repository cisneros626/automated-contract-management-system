import os
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

if not os.path.exists("contracts.db"):
    print("Database file not found. Creating a new database.")
    engine = create_engine(DATABASE_URL, echo=True)  # Create the engine
    Base.metadata.create_all(engine)  # Create all tables
else:
    print("Database file found. Connecting to the existing database.")
    engine = create_engine(DATABASE_URL, echo=False)

# Set up the session
Session = sessionmaker(bind=engine)
session = Session()