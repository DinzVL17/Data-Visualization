# Biological data visualization
import pandas as pd
dataset1 = pd.read_csv("BlackbirdTestosterone.csv")
print(dataset1["log before"].describe())
print(dataset1["log after"].describe())
print(dataset1["dif in logs"].describe())


# Histogram
import seaborn as sns
import matplotlib.pyplot as plt
sns.histplot(dataset1 ,kde=True, x=dataset1["dif in logs"])
plt.title("Histogram of BlackbirdTestosterone")
plt.show()


# Quantile-Quantile plot
from statsmodels.graphics.gofplots import qqplot
qqplot(dataset1["dif in logs"],xlabel="dif in logs", line="s")
plt.title("QQ plot of BlackbirdTestosterone")
plt.show()

# Shapiro-Wilk test
from scipy import stats
# stats, p = stats.shapiro(dataset1["dif in logs"])
# print("stats=%.3f, p-value=%.3f" %(stats,p))

# boxplot
fig, axs = plt.subplots(1,2,figsize=(12,4))
axs[0].boxplot(dataset1["Before"])
axs[0].set_title("Boxplot of before sample")
axs[1].boxplot(dataset1["After"])
axs[1].set_title("Boxplot of after sample")
plt.show()

# violin plots
fig, axs = plt.subplots(1,2, figsize=(12,4))
axs[0].violinplot(dataset1["Before"])
axs[0].set_title("Violin plot of before sample")
axs[1].violinplot(dataset1["After"])
axs[1].set_title("Violin plot of after sample")
plt.show()


# paired-sample t-test
t, p_value = stats.ttest_rel(dataset1["Before"],dataset1["After"], alternative= "greater")
print("t-statistics=%.3f, p-value=%.3f" %(t,p_value))



