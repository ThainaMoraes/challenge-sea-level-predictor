import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

df = pd.read_csv("epa-sea-level.csv")
df2 = df.query('Year>=2000')

x = df['Year']
y = df['CSIRO Adjusted Sea Level']

x2 = df2['Year']
y2 = df2['CSIRO Adjusted Sea Level']

def draw_plot():
    
    years_extended = np.arange(1880, 2051, 1)
    new_years_extended = np.arange(2000, 2051, 1)
    
    res = linregress(x, y)
    res2 = linregress(x2, y2)
    
    line = [res.slope*year + res.intercept for year in years_extended]
    line2 = [res2.slope*year + res2.intercept for year in new_years_extended]
    
    plt.scatter(x, y,  marker = 'o', label="Sample Point",)
    plt.plot(years_extended, line, color = 'orange', label="Fitting Line",linewidth=2 )
    plt.plot(new_years_extended, line2, color = 'red', label="Fitting Line 2",linewidth=2)
    
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel('Sea Level (inches)')
    plt.title("Rise in Sea Level")
        
    plt.savefig('sea_level_plot.png')
    return plt.gca()