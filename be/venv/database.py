from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/tms"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# def check_db_connection():
#     try:
#         # Try to establish a connection
#         with engine.connect() as connection:
#             connection.execute(text("SELECT 1"))
#         print("Database connection successful")
#     except OperationalError as e:
#         print(f"Database connection failed: {e}")

# # Check the connection
# check_db_connection()