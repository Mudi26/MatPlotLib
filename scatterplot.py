import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(50) * 100 #50 random values #Numbers are between 0 and 1, therefore *100. So it is 0-100
y_data = np.random.random(50) * 100 #50 random values #Numbers are between 0 and 1, therefore *100. So it is 0-100

#Scatter plot

print(x_data) #If we want to see coordinates

plt.scatter(x_data, y_data, c = "red", marker = "*", s=50) #Color can be defined in hexa, and RGB, and letters
#color, form of circles, size, alpha can be used to mark where there may be overlapping points.
plt.show() #This is only necessary if there is no JupyterLab