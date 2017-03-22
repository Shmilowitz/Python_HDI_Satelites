import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections, sys, operator, csv

database = pd.read_csv('database.csv',quotechar='"',skipinitialspace=True, delimiter=',', na_values='')
data = database.as_matrix()

print("Which country has the lightest satelite and how much does it weight?")
coun_weight = database[['Country of Operator/Owner', 'Launch Mass (Kilograms)']]


# coun_weight['Launch Mass (Kilograms)'] = pd.to_numeric(coun_weight['Launch Mass (Kilograms)'], errors='coerce')
coun_weight['Launch Mass (Kilograms)'] = coun_weight['Launch Mass (Kilograms)'].replace('5,000+', 5000).astype(float)
sys.stdout = open('Q4.txt', 'w')
print(data[np.argmin(coun_weight['Launch Mass (Kilograms)']),3], data[np.argmin(coun_weight['Launch Mass (Kilograms)']),15])
sys.stdout.close()
