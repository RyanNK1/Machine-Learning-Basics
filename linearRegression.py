import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 2.5, 3, 4]
y = [1, 4, 7, 9, 15]

plt.plot(x, y, 'ro')
'''
plt.plot(x, y, 'ro') — What It Does
This line plots your data points using matplotlib:

x and y are lists of coordinates.
'ro' is a format string:
'r' = red color
'o' = circle markers
So this line plots red circles at each (x, y) point
'''
plt.axis([0, 6, 0, 20])#Limits of the axes
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))#Line of Best fit
plt.show()
#plt.savefig("plot1.png") w/o line of best fit
plt.savefig("plot2.png")