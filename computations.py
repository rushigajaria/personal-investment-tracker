import quandl
import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import QUANDL_KEY, DB_FILEPATH
from init_db import Stock
quandl.ApiConfig.api_key = QUANDL_KEY

def portfolio_values_with_market():
    engine = create_engine(DB_FILEPATH)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    df_rows = []

    for stock in session.query(Stock).all():
        market_value = quandl.get('WIKI/%s' % stock.ticker,rows=1).Close.iloc[0] #this will give the latest data
        stock_dict = {"ticker":stock.ticker,
                      "quantity":stock.quantity,
                      "book_value":stock.book_value,
                      "market_value":market_value}
        df_rows.append(stock_dict)
    
    return pd.DataFrame(df_rows)               
    
def calculate_profit(_):
    df = portfolio_values_with_market()
    profit = 0
    for index, row in df.iterrows():
        profit += (row.market_value - row.book_value)*row.quantity
    
    print "Your portfolio return is $%s" % profit
    if profit == 0:
        print "No change in value"
    elif profit > 0:
        print "Your holdings have earned money :)"
    else:
        print "You have lost money :("

def buy_sell_recommendations(_):
    print portfolio_values_with_market()

if __name__ == "__main__":
    portfolio_values_with_market()