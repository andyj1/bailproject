import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def plotBail(df):
    """
    nysid	
    bond_info	- keep
    warrants
    arrest_date - keep
    next_court_date - keep
    housing_facility
    docket_numbers	
    charges - keep
    race - keep
    gender - keep
    is_new	
    contains eligible charge
    """
    # print(df.head())
    print('df shape is', df.shape)

    charges = df['charges'].values
    bonds = df['bond_info'].values

    # charges_first = np.zeros((len(charges),))

    # for idx in range(len(charges)):
    #     for i, c in enumerate(charges[idx]):
    #         if c == '(':
    #             start_idx = i
    #         elif c == ')':
    #             end_idx = i
    #         else:
    #             start_idx = 0
    #             end_idx = -1
    #         charges_first[idx] = charges[idx][start_idx+1 : end_idx] 

    # # extract specifically
    # idx = 0
    # for i, c in enumerate(charges[idx]):
    #     # start_idx = 0
    #     # end_idx = -1
    #     open_p_count = 0
    #     if c == '(':
    #         start_idx = i
    #     elif c == ')':
    #         end_idx = i
    # print(charges[idx][start_idx+1:end_idx])

    # crime = 'CRIM POSS MARIJUANA'
    # crime = 'CRIM POS'
    crime = 'MARIJUANA'
    crime_list = []

    for idx in range(len(charges)):
        if (crime in charges[idx]) and ('|' not in charges[idx]):
            crime_list.append(idx)

    print('number of {} crimes is {}'.format(crime, len(crime_list)))

    bond_tot = 0

    for idx in crime_list:
        print(charges[idx])
        bond_tot += bonds[idx]
    
    bond_avg = bond_tot / len(crime_list)

    print('The total bond amount is {} with an average of {} from {} charges'.format(bond_tot, bond_avg, len(crime_list)))



def main():
    df = pd.read_csv('data/nyc_parsed.csv')
    plotBail(df)

if __name__ == "__main__":
    main()