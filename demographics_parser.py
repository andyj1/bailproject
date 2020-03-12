import pandas as pd
import math
import numpy as np

def main():
    df = pd.read_csv('data/psam_p22.csv')
    # print(df.head())

    df_trim = df[['RAC1P', 'PWGTP', 'ADJINC']]
    print(df_trim.head())

    # race = df['RAC1P'].values
    # print(len(race))

    # count = 0
    # for idx in range(len(race)):
    #     if not math.isnan(race[idx]):
    #         count += 1
    
    # print('count', count)

    # Print all column names
    # for col in df.columns:
        # print(col)

# RAC1P
# Recoded detailed race code 
# 1 .White alone 
# 2 .Black or African American alone 
# 3 .American Indian alone 
# 4 .Alaska Native alone 
# 5 .American Indian and Alaska Native tribes specified; or   .American Indian or Alaska Native, not specified and no other   .races 
# 6 .Asian alone 
# 7 .Native Hawaiian and Other Pacific Islander alone 
# 8 .Some Other Race alone 
# 9 .Two or More Races 

# WAGP Numeric 6 
# Wages or salary income past 12 months (use ADJINC to adjust WAGP to constant dollars) 
# bbbbbb .N/A (less than 15 years old) 
# 0 .None 
# 4..999999 .$4    to 999999 (Rounded and top-coded) 

if __name__ == "__main__":
    main()