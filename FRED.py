# import stuff
import pandas as pd
from fredapi import Fred
import seaborn as sns

# api setup
mykey = 'd7bfb2556104ea5614540a00d6def805'
fred = Fred(api_key=mykey)

# test input
# gdp = raw_input('What would you like to test?')

# get data
SP500 = fred.get_series('SP500',observation_start='2005-01-01')
CPI = fred.get_series('CPIAUCSL',observation_start='2005-01-01')
GDP = fred.get_series('GDP',observation_start='2005-01-01')

# setup full dataframe + organize by removing NaN
df = pd.concat([CPI,GDP],join='outer',axis=1)
df2 = df.dropna()
df2.columns = ['CPI','GDP']


# create percent change values
df2['CPI CHANGE'] = df2['CPI'].pct_change()
df2['GDP CHANGE'] = df2['GDP'].pct_change()



###***PLOTTING PRACTICE

### visualize a distribution
# verified
# distplot = sns.distplot(df2['SP500'],bins=30)

### joint plot is scatter plot comparing two columns of data
# verified it works
# jointplot = sns.jointplot(x='SP500 CHANGE',y='CPI CHANGE',data=df2,kind='hex')

###pair plot compares all values
# pairplot = sns.pairplot(df2,hue='sex',palette='coolwarm')

###rug plots like a vertical histogram
# rug = sns.rugplot(df2['CPI CHANGE'])

###*** correlations + regressions
reg = df2.corr()
heat = sns.heatmap(reg,cmap='coolwarm',linecolor='white',linewidth=1)

sns.plt.show()
