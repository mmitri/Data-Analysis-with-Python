import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="green")

    # Create first line of best fit
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    year2050 = np.arange(df["Year"].min(), 2051)
    y_hat = res.slope*year2050 + res.intercept
    plt.plot(year2050, y_hat, color="red")

    # Create second line of best fit
    df2000 = df[(df["Year"] >= 2000) & (df["Year"] <= 2051)]
    res2000 = linregress(df2000["Year"], df2000["CSIRO Adjusted Sea Level"])
    year2000 = np.arange(2000, 2051)
    y_hat2000 = res2000.slope*year2000 + res2000.intercept
    plt.plot(year2000, y_hat2000, color="blue")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()