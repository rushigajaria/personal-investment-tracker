#Run this first
import sqlite3
from sqlite3 import Error
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd

from config import DB_FILEPATH, DB_FILE, PORTFOLIO_FILE

#Setup DB File
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print "Database file created successfully"
    except Error as e:
        print(e)
    finally:
        conn.close()

create_connection(DB_FILE)

#Create Portfolio Table
Base = declarative_base()
 
class Stock(Base):
    __tablename__ = "portfolio"
    id = Column(Integer, primary_key=True)
    ticker = Column(String(10), nullable=False)
    book_value = Column(Float)
    quantity = Column(Integer, nullable=False)

engine = create_engine(DB_FILEPATH)
Base.metadata.create_all(engine)
print "Table created successfully"
