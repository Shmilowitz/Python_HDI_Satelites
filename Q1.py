import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections, sys

database = pd.read_csv('historical_index.csv',quotechar='"',skipinitialspace=True, delimiter=',')
data = database.as_matrix()
# Which country has the highest HDI (Human Development Index) and which has the lowest?

print("Which country has the highest HDI (Human Development Index) and which has the lowest?")
HDI2014 = database[['Country', 'Human Development Index (2014)']]
HDI2014max = np.amax(HDI2014['Human Development Index (2014)'])
HDI2014min = np.amin(HDI2014['Human Development Index (2014)'])
print(HDI2014min)
sys.stdout = open('Q1.txt', 'w')
for r in data:
	if r[8] == HDI2014max:
		print('The country with the highest HDI is {} with {}'.format(r[1], "%.3f" % r[8]))
	elif r[8] == HDI2014min:
		print('The country with the lowest HDI is {} with {}'.format(r[1], "%.3f" % r[8]))
sys.stdout.close()
