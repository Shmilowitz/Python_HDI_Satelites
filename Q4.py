import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections, sys, operator, csv

database = pd.read_csv('database.csv',quotechar='"',skipinitialspace=True, delimiter=',', na_values='')

print("Which country has the lightest satelite and how much does it weight?")
coun_weight = database[['Country of Operator/Owner', 'Launch Mass (Kilograms)']]

# print(coun_weight)
coun_weight['Launch Mass (Kilograms)'] = pd.to_numeric(coun_weight['Launch Mass (Kilograms)'], errors='coerce')

lightest = np.nanmin(coun_weight['Launch Mass (Kilograms)'].replace('5,000+', 5000).astype(float))
print(lightest)
print (coun_weight['Launch Mass (Kilograms)'].iloc[1091:1098])
