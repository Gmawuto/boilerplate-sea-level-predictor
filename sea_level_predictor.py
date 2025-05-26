import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(x=df["Year"],y=df["CSIRO Adjusted Sea Level"])
    plt.xlabel("Year")
    plt.ylabel("CSIRO Adjusted Sea Level")
    plt.title("CSIRO Adjusted function of years")

    # Create first line of best fit
    #get slope and intercept
    model = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    slope, intercept = float(model.slope), float(model.intercept)

    x_pred = np.arange(df['Year'].min(), 2051)  # 1880 to 2050
    y_pred = slope * x_pred + intercept
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot original scatter
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', alpha=0.6)
    
    # Plot line of best fit
    ax.plot(x_pred, y_pred, 'r', label='Best Fit Line (to 2050)')
    

    # Create second line of best fit
    x_pred = np.arange(df['Year'].min(), 2051)  # 1880 to 2050
    y_pred = slope * x_pred + intercept
    
    x__pred=np.arange(2000, 2051)
    y__pred=slope * x__pred + intercept
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    year=df["Year"].max()
    # Plot original scatter
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', alpha=0.6)
    
    # Plot line of best fit
    ax.plot(x_pred, y_pred, 'r', label='Best Fit Line (to 2050)')
    ax.plot(x__pred,y__pred,"g", label= f"Best Fit Line from 2000 to 2050 but passing through {year} recent year")

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.legend()
    plt.grid(True)
    plt.tight_layout()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
