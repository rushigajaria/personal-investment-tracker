import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import datetime
import pandas as pd
import numpy as np
from computations import portfolio_values_with_market

def graph(_):
    df = portfolio_values_with_market()
    # Setting the positions and width for the bars
    pos = list(range(len(df['market_value']))) 
    width = 0.25 
        
    # Plotting the bars
    fig, ax = plt.subplots(figsize=(10,5))


    # Create a bar with mid_score data,
    # in position pos + some width buffer,
    plt.bar([p + width for p in pos], 
            #using df['mid_score'] data,
            df['book_value'],
            # of width
            width, 
            # with alpha 0.5
            alpha=0.5, 
            # with color
            color='#F78F1E', 
            # with label the second value in first_name
            label=df['ticker'][1]) 

    # Create a bar with post_score data,
    # in position pos + some width buffer,
    plt.bar([p + width*2 for p in pos], 
            #using df['post_score'] data,
            df['market_value'], 
            # of width
            width, 
            # with alpha 0.5
            alpha=0.5, 
            # with color
            color='#FFC222', 
            # with label the third value in first_name
            label=df['ticker'][2]) 

    # Set the y axis label
    ax.set_ylabel('Value in USD')

    # Set the chart's title
    ax.set_title('Book vs Market Values')

    # Set the position of the x ticks
    ax.set_xticks([p + 1.5 * width for p in pos])

    # Set the labels for the x ticks
    ax.set_xticklabels(df['ticker'])

    # Setting the x-axis and y-axis limits
    plt.xlim(min(pos)-width, max(pos)+width*4)
    plt.ylim([0, max(df['book_value'] + df['market_value'])] )

    # Adding the legend and showing the plot
    plt.legend(['Book Value', 'Market Value'], loc='upper left')
    plt.grid()
    plt.show()

