import numpy as np
import matplotlib.pyplot as plt

ages = np.random.normal(20, 1.5, 1000) #mean = 20, standard deviation = 1.5, 1000 samples

plt.hist(ages, bins=[ages.min(), 18, 20, 22, ages.max()]) #Her laver man kategorierne selv
#plt.hist(ages, cumulative=True) # Den går opad, og regner procentmæssigt.
plt.show()

##ABC