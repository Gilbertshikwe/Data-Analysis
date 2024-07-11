# bokeh_plots.py

from bokeh.plotting import figure, show, output_file
import numpy as np
import pandas as pd

# Set the output file
output_file("bokeh_plots.html")

# Line Plot
p = figure(title="Line Plot", x_axis_label='X-axis', y_axis_label='Y-axis')
p.line([1, 2, 3, 4, 5], [10, 15, 13, 17, 19], legend_label='Trend', line_width=2)
show(p)

# Bar Plot
categories = ['A', 'B', 'C', 'D', 'E']
values = [4, 7, 1, 8, 5]
p = figure(x_range=categories, title="Bar Plot", x_axis_label='Categories', y_axis_label='Values')
p.vbar(x=categories, top=values, width=0.5)
show(p)

# Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)
p = figure(title="Scatter Plot", x_axis_label='X-axis', y_axis_label='Y-axis')
p.scatter(x, y, size=10)
show(p)

# Histogram
data = np.random.randn(1000)
hist, edges = np.histogram(data, bins=30)
p = figure(title="Histogram", x_axis_label='Value', y_axis_label='Frequency')
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="navy", line_color="white")
show(p)

# Box Plot
data = pd.DataFrame({
    'categories': ['A']*10 + ['B']*10 + ['C']*10,
    'values': np.random.rand(30)
})
p = figure(title="Box Plot", x_axis_label='Category', y_axis_label='Value')
p.vbar(x=data['categories'], top=data['values'], width=0.5)
show(p)
