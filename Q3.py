import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections, sys, operator

database = pd.read_csv('database.csv',quotechar='"',skipinitialspace=True, delimiter=',')
data = database.as_matrix()

print("Which country has the most satelites for military usage?")
mask = (data[:,4] == 'Military')
country = collections.Counter(data[mask][:,3])
print(country.most_common())

objects = [country.most_common()[x][0] for x in range(15)]
performance = [country.most_common()[x][1] for x in range(15)]

y_pos = np.arange(len(objects))

plt.bar(y_pos, performance, align='center', alpha=0.5)
for a,b in zip(y_pos, performance):
	plt.text(a-0.25, b+2, str(b))
plt.xticks(y_pos, objects, rotation=90, fontsize = 7)
plt.ylabel('Amount of satelites used')
plt.title('Satelites with military usage per country')
plt.savefig('Question3Chart.png', bbox_inches='tight')
#Saved version is scaled so everything can be seen properly compared to "show" version
#plt.show()