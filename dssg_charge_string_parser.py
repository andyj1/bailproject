import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def parseChargeCode(df):
    """
    Function that searches through "Charge" column of DataFrame
    for list of keywords and returns a trimmed DataFrame containing
    only the rows that contained a keyword
    """
    # print(df.head())
    charges = df["Charge"].values

    keywords_list = ["MURDER", "ASSAULT", "RAPE", "INTOXICATION"]
    parsed_charge_list = []
    keep_list = []

    # Find keyword in the data
    idx = 0
    for charge in charges:
        charge = str(charge) # handle rouge floats
        word_list = charge.split(' ')
        for word in word_list:
            for keyword in keywords_list:
                if keyword == word:
                    parsed_charge_list.append(charge)
                    keep_list.append(idx)
        idx += 1

    # find negative of keep_list (pop_list) to remove irrelevant charges
    pop_list = range(0, len(charges))
    for idx in pop_list:
        if idx in keep_list:
            pop_list.remove(idx)

    # # some more useful print statements
    # print(parsed_charge_list)
    # print("number of total charges: {}".format(len(charges)))
    # print("number of charges with {} keywords: {} (could contain\
    #     duplicates)".format(len(keywords_list), len(parsed_charge_list)))

    # Drop indices from DataFrame
    df.drop(pop_list, axis=0, inplace = True)

    return df

def readCrimeTypes(df):
    # BJ
    # bjs_description
    # bjs_category
    # Broad Category

    broad_category = df["Broad Category"].values
    return broad_category

# def countBail(df):

def main():
    # # read in data and parse by charge keyword
    # df_ar = pd.read_csv("data/AR_Washington_Charges_Cleaned.csv")
    # print('DataFrame size before: {}'.format(df_ar.shape))
    # df_ar_trimmed = parseChargeCode(df_ar)
    # print('DataFrame size after parsing {}'.format(df_ar_trimmed.shape))

    # df_bjs = pd.read_csv("data/BJS Offense_Code_Crosswalk")
    # bjs_crime_types = readCrimeTypes(df_bjs)
    # print(bjs_crime_types)

    df_census = pd.read_csv(StringIO("data/l08puw8.dat"), 
                sep="\s+", #separator whitespace
                index_col=0,
                header=None)
    
    print(df_census.head())

if __name__ == "__main__":
    main()