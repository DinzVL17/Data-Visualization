'''
Title: Analyze, describe, and visualize biological data and perform biological hypothesis testing.
Author: Dinuri Vishara
Date: 25/01/2023
'''

# Import the data set into a Pandas DataFrame
import pandas as pd
dataset1 = pd.read_csv("Temperature.csv")
print(dataset1.describe())

# draw the histogram for the variable
import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(dataset1,x="temperature",kde=True)
plt.title("Histogram of temperature variable")
plt.show()

# draw a Quantile-Quantile plot
from statsmodels.graphics.gofplots import qqplot
qqplot(dataset1,line="s")
plt.title("QQ plot of temperature")
plt.show()

# Shapiro-Wilk test
from scipy import stats
t,p= stats.shapiro(dataset1)
print("stats=%.3f P-value=%.3f" %(t,p))

# One-sampe t-test
test, p = stats.ttest_1samp(dataset1, popmean=98.6, alternative='two-sided')
print("Test-statistics:",test,"p-value:",p)




