import pandas as pd


print("helllo")

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()

data = [i.split(',') for i in data]


column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)


df['Alcohol']=df['Alcohol'].astype(float)
df['Tobacco']=df['Tobacco'].astype(float)

print("Alcohol Mean:",df['Alcohol'].mean())
print("Tobacco Mean:",df['Tobacco'].mean())

print("Alcohol Median:",df['Alcohol'].median())
print("Tobacco Median:",df['Tobacco'].median())


print("Alcohol Range:",df['Alcohol'].max()-df['Alcohol'].min())
print("Tobacco Range:",df['Tobacco'].max()-df['Tobacco'].min())


print("Alcohol standard deviation:",df['Alcohol'].std())
print("Tobacco standard deviation:",df['Tobacco'].std())

print("Alcohol variance:",df['Alcohol'].var())
print("Tobacco variance:",df['Tobacco'].var())
