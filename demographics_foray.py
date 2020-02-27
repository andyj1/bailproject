import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
This data was obtained through the American Community Survey (ACM)
Demographic information src here:
https://data.census.gov/cedsci/table?d=ACS%205-Year%20Estimates%20Data%20Profiles&table=DP05&tid=ACSDP5Y2018.DP05&g=0400000US22_1600000US2205000
"""

def plotRaceDemographics(dict, pop, title):
    labels = ['white', 'black', 'other']
    data =   [dict['white'], dict['black'], dict['other']]
    colors = ['orange', 'blue', 'green']
    
    plt.pie(data, labels=labels, colors=colors, autopct='%1.1f%%', startangle=180)
    plt.title('{} Race Distribution, Total Population is {}'.format(title, pop))
    plt.axis('equal')


def main():
    ### Baton Rouge LA ###
    la_total_pop = 225361

    la_race_dict = {
        "white": 82419,
        "black": 123580,
        # "hispanic": 8309, # Do we want to use this?
    }
    if 'other' not in la_race_dict.keys():
        la_race_dict['other'] = la_total_pop - sum(la_race_dict.values())

    ## NYC ###

    nyc_total_pop = 8443713

    nyc_race_dict = {
        "white": 3809219,
        "black": 2190875,
        # "hispanic": 2457137, # Do we want to use this?
    }
    if 'other' not in nyc_race_dict.keys():
        nyc_race_dict['other'] = nyc_total_pop - sum(nyc_race_dict.values())


    # plotRaceDemographics(la_race_dict, la_total_pop, 'Baton Rouge, LA')
    plotRaceDemographics(nyc_race_dict, nyc_total_pop, 'New York City, NY')

    plt.show()

if __name__ == "__main__":
    main()