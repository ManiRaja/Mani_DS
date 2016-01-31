import collections
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


testlist = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(testlist)

print(c)

# calculate the number of instances in the list
count_sum = sum(c.values())

for k,v in c.items():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))

plt.boxplot(testlist)
plt.show()


plt.hist(testlist, histtype='bar')
plt.show()

graph1 = stats.probplot(testlist, dist="norm", plot=plt)
plt.show() #this will generate the first graph


