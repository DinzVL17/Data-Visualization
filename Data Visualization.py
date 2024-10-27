### Data Visualization
# Import the data set into a Pandas DataFrame
import matplotlib.pyplot as plt
import pandas as pd


dataset2 = pd.read_csv("HornedLizards.csv")
dataset2 = dataset2.dropna()

# statistics for horn lengths of the living lizards
survived = dataset2[dataset2["Survive"] == "survived"]
print(survived.describe())

# statistics for horn lengths of the dead lizards
dead = dataset2[dataset2["Survive"] == "dead"]
print(dead.describe())


import seaborn as sns
fig, axs = plt.subplots(1,2,figsize=(12,4))
# Histogram for horn lengths of the living lizards
sns.histplot(survived,kde=True,ax=axs[0])
axs[0].set_title("Histogram of horn lengths of the living lizards")
# Histogram for horn lengths of the dead lizards
sns.histplot(dead,kde=True,ax=axs[1])
axs[1].set_title("Histogram of horn lengths of the dead lizards")
plt.show()


# QQ plot
from statsmodels.graphics.gofplots import qqplot
fig, axs = plt.subplots(1,2, figsize=(12,4))
# QQ-plot for horn lengths of the living lizards
qqplot(survived["Squamosal horn length"],line="s",ax=axs[0])
axs[0].set_title("QQ-plot of horn lengths of the living lizards")
# QQ-plot for horn lengths of the dead lizards
qqplot(dead["Squamosal horn length"],line="s",ax=axs[1])
axs[1].set_title("QQ-plot of horn lengths of the dead lizards")
plt.show()

# Shapiro-Wilk test
from scipy import stats
stat_s, ps = stats.shapiro(survived["Squamosal horn length"])
print("stats=%.3f, p-value=%.3f" %(stat_s,ps))

stats_d, pd = stats.shapiro(dead["Squamosal horn length"])
print("stats=%.3f P-value=%.3f" %(stats_d,pd))

# Boxplot
fig, axs = plt.subplots(1,2, figsize=(12,4))
axs[0].boxplot(survived["Squamosal horn length"])
axs[0].set_title("Boxplot of survived sample")
axs[1].boxplot(dead["Squamosal horn length"])
axs[1].set_title("Boxplot of dead sample")
plt.show()

# violin plots
fig, axs = plt.subplots(1,2, figsize=(12,4))
axs[0].violinplot(survived["Squamosal horn length"])
axs[0].set_title("Violin plot of survived sample")
axs[1].violinplot(dead["Squamosal horn length"])
axs[1].set_title("Violin plot of dead sample")
plt.show()

# Mann Whitney u test
import scipy.stats as stats
stats, p = stats.mannwhitneyu(survived["Squamosal horn length"],
           dead["Squamosal horn length"],alternative="two-sided")
print("stats=%.3f P-value=%.3f" %(stats,p))

