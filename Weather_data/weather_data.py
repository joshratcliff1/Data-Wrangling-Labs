import pandas as pd
import matplotlib.pyplot as plt

# show complete records by changing rules
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
#pd.set_option('display.max_colwidth', -1)

df = pd.read_csv("weather.csv")

# Read the first 5 rows of data
print(df.head(5))

# Read the last 5 rows of data
print(df.tail(5))

# Read 3 rows of data. From row 5 to row upto but not including 8. (Similar to slicing)
print(df[5:8])


# print the contents of a single column. 2 ways
print(df.Location)
print(df['Location'])

'''
Note, you can display the values for the following information
dtypes - List the types of the columns
columns - List the column names
axes - List the row labels and column names
size - Number of elements
'''

# as an example
print(df.dtypes)
print(df.size)


# The below will display the rows that have any missing values (Displayed as NaN - Not a Number)
print(df[df.isnull().any(axis=1)])

# The below will display rows that have missing values in all columns (note, there aren't any)
print(df[df.isnull().all(axis=1)])

# Provides basic statistics on a single variable
print(df['MaxTemp'].describe())

# Provides basic statistics on multiple variables (note the double braces).
print(df[['MaxTemp', 'MinTemp']].describe())

# Provides a decimal value for the correlation between two variables
print(df['MaxTemp'].corr(df['MinTemp']))

# Provides a list
print(df['WindGustDir'].unique())

'''
Some more useful opperators:
(listed in the Lab pdf)
'''

'''Plotting'''

# Plot a histogram of an attribute
#df['MaxTemp'].plot(kind='hist', bins=50)
#df['MaxTemp'].plot.hist(bins=50)

# Plot a histogram of multiple attributes
#df[['MaxTemp','MinTemp']].plot(kind='hist', bins=50)
df[['MaxTemp','MinTemp']].plot.hist(bins=50)
plt.savefig('test.jpg')

# Plot a box plot for multiple attributes
#df[['MaxTemp','MinTemp']].plot(kind='box')
#df[['MaxTemp','MinTemp']].plot.box()

# Plot a density distribution
#df['MaxTemp'].plot.kde()


# required to show the created plots
plt.show()