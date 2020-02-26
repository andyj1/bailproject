import pandas as pd
# pandas.__version__
import numpy as np
import matplotlib.pyplot as plt

nyc_charges = pd.read_csv("data/2_4 data NYC.csv")
# raw_ny = pd.read_csv(r"C:\data_folder\nyctrend.csv")
# nytr = pd.read_csv(r"C:\data_folder\nyctrend.csv")

print(nyc_charges.head())

bond_info = nyc_charges["bond_info"].values

pop_list = []

for idx in range(len(bond_info)):
    if type(bond_info[idx]) is str:
        pop_list.append(idx)

df.drop(pop_list, axis=0, inplace = True)