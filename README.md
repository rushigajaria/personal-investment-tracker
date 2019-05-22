# Rate These Stocks
*A simple Python command-line program designed to help view data about stocks*

## Setup
Navigate to the root directory of the project and ensure you have specified the correct variables in config.py and have created a CSV file from which to seed the database.

Then, initialize the database with
```
python init_db.py
```

Next, you will need to load your data into the database with
```
python seed_db.py
```


## Usage
Navigate to the root directory of the project and run the program using
```
python app.py
```

Then, you can enter whichever command you would like to run. Type help to see what is available. 


## How It Works
The script runs based on the portfolio you specify in the database. It then pulls market data from the Quandl Finance API. 


## Prerequisites

To run the program, ensure you have installed the Quandl Finance Python library to access the API
```
pip install quandl
```

Created for educational purposes.