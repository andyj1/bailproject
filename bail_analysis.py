import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def find_drug_degree(df):
    """
    Returns avgerage bail bond amount 

    nysid	
    bond_info	     - keep
    warrants
    arrest_date      - keep
    next_court_date  - keep
    housing_facility
    docket_numbers	
    charges          - keep
    race             - keep
    gender           - keep
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
    # crime = 'MARIJUANA'

    # degree 7, 5, 4, 3, 2, 1
    drug_sch_list = ['220.03', '220.06', '220.09', '220.16', '220.18', '220.21']
    degree_list = ['7th', '5th', '4th', '3rd', '2nd', '1st']
    bond_avg_list = []
    bond_tot_list = []
    counts_list = []

    for crime in drug_sch_list:
        # find indices in the DataFrame that match the charge code
        crime_list = []
        for idx in range(len(charges)):
            if (crime in charges[idx]) and ('|' not in charges[idx]):
                crime_list.append(idx)

        # collect total bond amount information by matchign indices
        bond_tot = 0
        for idx in crime_list:
            print(charges[idx])
            print(bonds[idx])
            bond_tot += bonds[idx]
        
        bond_tot_list.append(bond_tot)
        # handle division by zero if there are no crimes within list
        if len(crime_list) != 0:
            bond_avg = float(bond_tot) / float(len(crime_list))
        else:
            bond_avg = 0
        print('The total bond amount is {} with an average of {} from {} charges'.format(bond_tot, bond_avg, len(crime_list)))

        bond_avg_list.append(bond_avg)
        counts_list.append(len(crime_list))

    drug_sch_list.append('220.03 & 220.06')
    degree_list.append('7th & 5th')
    bond_tot_list.append(bond_tot_list[0] + bond_tot_list[1])
    counts_list.append(counts_list[0] + counts_list[1])
    bond_avg_list.append((float(bond_tot_list[0]) + float(bond_tot_list[1])) / \
        (float(counts_list[0]) + float(counts_list[1])))


    df_res = pd.DataFrame({'statute':  drug_sch_list,
                           'counts':   counts_list,
                           'avg_bond': bond_avg_list,
                           'degree':   degree_list,
    })

    print(df_res)
    df_res.to_csv('data/nyc_drug_degree.csv ')

def find_dollar_bail(df):
    # print(df.head())
    print('df shape initially is', df.shape)

    # charges = df['charges'].values
    # bonds = df['bond_info'].values
    # low_bond_idx_list = []
    # for idx in range(len(bonds)):
    #     if bonds[idx] < 10.:
    #         low_bond_idx_list.append(idx)
    # print(low_bond_idx_list)

    df2 = df.loc[df['bond_info'] < 10.]
    print(df2.head())
    print('df shape after is', df2.shape)

    # bonds = df2['bond_info'].values

    # df3 = df2.loc[df['charges'].isin(['Felony'])]
    # print(df3.head())

    felony_count = df2['charges'].str.contains('Felony').sum()
    if felony_count > 0:
        print('There are {} Felony counts'.format(felony_count))

    misdemeanor_count = df2['charges'].str.contains('Misdemeanor').sum()
    if misdemeanor_count > 0:
        print('There are {} Misdemeanor counts'.format(misdemeanor_count))

def main_nyc():
    df = pd.read_csv('data/nyc_parsed.csv')
    # find_drug_degree(df)
    find_dollar_bail(df)

def main_la():
    df = pd.read_csv('data/la_parsed')

if __name__ == "__main__":
    main_nyc()