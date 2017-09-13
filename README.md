# Rate These Stocks
*A simple Python command-line program designed to rank stocks

## Usage
Navigate to the directory with the Python file and run it using
```
python rate_these_stocks.py
```

Next, you will be prompted to enter the tickers of stocks you are interested in. For example, if we are interested in Google, Facebook, and Microsoft, we would enter
```
GOOG, FB, MSFT
```

The result will be an array sorted from highest to lowest by score (explained later).

## How It Works
The script takes in the tickers and then iterates through them and calculates a score for each stock. Then, the script will simply sort these tickers by their score. 

## Troubleshooting

To run the program, ensure you have installed the Yahoo Finance python library to access the API
```
pip install yahoo-finance
```
