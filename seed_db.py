from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd

from config import PORTFOLIO_FILE, DB_FILEPATH
from init_db import Stock

#Load data into table
engine = create_engine(DB_FILEPATH)
df = pd.read_csv(PORTFOLIO_FILE)
DBSession = sessionmaker(bind=engine)
session = DBSession()
for index, row in df.iterrows():
    new_person = Stock(ticker=row.ticker,
                       book_value=row.book_value,
                       quantity=row.quantity)
    session.add(new_person)
session.commit()
print "Populated Database with your portfolio data"