import matplotlib.pyplot as plt
import numpy as np

# Line Plot
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 19]
plt.figure()
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.savefig('line_plot.png')  # Save the plot
plt.close()

# Bar Plot
categories = ['A', 'B', 'C', 'D', 'E']
values = [4, 7, 1, 8, 5]
plt.figure()
plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.savefig('bar_plot.png')  # Save the plot
plt.close()

# Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)
plt.figure()
plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.savefig('scatter_plot.png')  # Save the plot
plt.close()

# Histogram
data = np.random.randn(1000)
plt.figure()
plt.hist(data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.savefig('histogram.png')  # Save the plot
plt.close()

# Box Plot
data = np.random.rand(10, 5)
plt.figure()
plt.boxplot(data)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Box Plot')
plt.savefig('box_plot.png')  # Save the plot
plt.close()
