import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def parse_df(df):
    """
    Parses through df to remove nan and non-numeric bail amounts

    Keep only the following columns
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
    print(df.head())
    print(df.shape)

    df.drop(['nysid', 'warrants', 'housing_facility', 'docket_numbers', 'is_new', \
        'contains eligible charge'], axis=1, inplace=True)

    print(df.head())
    print(df.shape)

    bond_info = df["bond_info"].values
    # bond_info = bond_info.astype(int)
    # print(type(bond_info[4]))
    print(len(bond_info))
    print(bond_info)

    print(bond_info[4].isdigit())
    print(math.isnan(bond_info[-1]))

    # parse through bail amounts to find numeric values
    nan_list = []
    int_list = []
    other_list = []
    for idx in range(len(bond_info)):
        # handle strings
        if type(bond_info[idx]) == str:
            if bond_info[idx].isdigit():
                # print('found an int')
                int_list.append(idx)
            else:
                # print('found an other')
                other_list.append(idx)
        
        # handle nans
        else:
            # print('found a float')
            nan_list.append(idx)
    
    print('length of nan list', len(nan_list))
    print('length of int list', len(int_list))
    print('length of other list', len(other_list))

    print('df shape before', df.shape)
    df.drop(other_list, axis=0, inplace = True)
    df.drop(nan_list, axis=0, inplace = True)
    print('df shape after', df.shape)

    # # remove rows that have nan's for charges
    # charges = df["charges"].values
    # nan_list_charges = []
    # for idx in range(len(charges)):
    #     if type(charges[idx]) == float:
    #         nan_list_charges.append(idx)
    # print('length of charges nan list', len(nan_list_charges))

    # # pop nans and view size of df before and after
    # print('df shape before', df.shape)
    # df.drop(nan_list_charges, axis=0, inplace = True)
    # print('df shape after', df.shape)

    # save out data to new csv
    df.to_csv('data/nyc_parsed.csv')


def main():
    df = pd.read_csv("data/2_4 data NYC.csv")
    parse_df(df)


if __name__ == "__main__":
    main()