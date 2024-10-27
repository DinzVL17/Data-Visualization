## Biological data visualization
import pandas as pd

df = pd.DataFrame({
    "count":[1,10,37,49,35,9],
    "Infection_level":["uninfected","lightly_infected","highly_infected","uninfected","lightly_infected","highly_infected"],
    "Eaten by birds":["eaten","eaten","eaten","not-eaten","not-eaten","not-eaten"]
    })
# Create the contingency table
dataframe= df.pivot_table(index="Eaten by birds", columns="Infection_level",values="count")
print(dataframe)


import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

# create a dictionary from dataframe
dataframe_dict = dict(dataframe.stack(level=-1, dropna=True))

# draw a mosaic plot
mosaic = mosaic(dataframe_dict , title='Mosaic plot')
plt.show()

# Chi-square contingency test
from scipy.stats import chi2_contingency
stats, p, dof, expected = chi2_contingency(dataframe)
print("Chi-square statistic:", stats)
print("P-value:", p)
print("Degrees of freedom:", dof)

# Output the expected value table
expectedValues = pd.DataFrame(expected, index=["eaten","not-eaten"],
                              columns=["uninfected","lightly_infected","highly_infected"])
print(expectedValues)







