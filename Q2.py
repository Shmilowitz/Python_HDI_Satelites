import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections, sys, operator
from heapq import nlargest
from operator import itemgetter

database = pd.read_csv('historical_index.csv',quotechar='"',skipinitialspace=True, delimiter=',')
data = database.as_matrix()

#Plot Generator
objectsContainer = []
performanceContainer = []
dictData = {}
dict30 = {}

#Adding data into dictData
for x in data:
	if x[2] != "..":
		dictData[x[1]] = "%.3f" % (float(x[8]) - float(x[2]))

#Making a dictDataionary with top 30 progression
for name, score in nlargest(30, dictData.items(), key=itemgetter(1)):
    dict30[name] = score
print(dict30)

# objects = [dict30[x][0] for x in range(30)]
# performance = [dict30[x][1] for x in range(30)]

d = {k:float(v) for k, v in dict30.items()}


y_pos = range(len(d))
plt.bar(y_pos, d.values(), align='center', alpha=0.5)
plt.xticks(y_pos, d.keys(), rotation=90, fontsize = 7)
plt.ylabel('HDI progression')
plt.title('HDI raised by contries')
plt.savefig('Question2.png', bbox_inches='tight')
plt.show() 


