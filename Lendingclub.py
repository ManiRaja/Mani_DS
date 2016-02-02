import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True) # drop rows with null values

#Box Plot
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()

#print(loansData["Amount.Funded.By.Investors"])

#Histogram
loansData.hist(column='Amount.Funded.By.Investors', histtype='bar')
plt.show()

# QQ Plot
graph1 =stats.probplot(loansData["Amount.Funded.By.Investors"], dist="norm", plot=plt)
plt.show() #this will generate the first graph
