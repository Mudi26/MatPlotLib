import numpy as np
import matplotlib.pyplot as plt

years = [2014 + x for x in range(9)] #9 years forward
weights = [80,83,84,85,81,89,78,80,77]

print(len(years))
print(len(weights))

plt.plot(years,weights, c="y", lw = 3, linestyle = "--") #To make lineplot
#color, lineWidth, linestyle
#plt.plot(years,weights, c="r--", lw = 3)
plt.show()

#plt.scatter(years,weights) # to make scatter plots

