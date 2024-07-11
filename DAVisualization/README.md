# Data Visualization with Python

Data visualization is a crucial aspect of data analysis, allowing for the effective communication of insights derived from data. It involves the graphical representation of data to highlight patterns, trends, and correlations that might not be apparent in raw data. This README introduces four popular Python libraries used for data visualization: Matplotlib, Plotly, Seaborn, and Bokeh.

## Table of Contents

1. [Matplotlib](#matplotlib)
2. [Plotly](#plotly)
3. [Seaborn](#seaborn)
4. [Bokeh](#bokeh)
5. [Summary](#summary)

### 1. Matplotlib

Matplotlib is one of the most widely used libraries for data visualization in Python. It provides a comprehensive range of plotting functions and is highly customizable.

**Installation:**

```bash
pip install matplotlib
```

**Basic Usage:**

```python
import matplotlib.pyplot as plt

# Simple line plot
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 19]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()
```

### 2. Plotly

Plotly is a library that allows for interactive and web-based data visualizations. It is great for creating complex and dynamic plots that can be embedded in web applications.

**Installation:**

```bash
pip install plotly
```

**Basic Usage:**

```python
import plotly.graph_objects as go

# Simple line plot
fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4, 5], y=[10, 15, 13, 17, 19], mode='lines+markers'))
fig.update_layout(title='Simple Line Plot', xaxis_title='X-axis', yaxis_title='Y-axis')
fig.show()
```

### 3. Seaborn

Seaborn is built on top of Matplotlib and provides a high-level interface for drawing attractive and informative statistical graphics. It is particularly well-suited for visualizing complex datasets.

**Installation:**

```bash
pip install seaborn
```

**Basic Usage:**

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
tips = sns.load_dataset('tips')

# Simple scatter plot
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Scatter Plot of Total Bill vs Tip')
plt.show()
```

### 4. Bokeh

Bokeh is designed for creating interactive and highly versatile visualizations that can be outputted to HTML files or integrated into web applications.

**Installation:**

```bash
pip install bokeh
```

**Basic Usage:**

```python
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

output_notebook()  # To display plots in Jupyter notebooks

# Simple line plot
p = figure(title="Simple Line Plot", x_axis_label='X-axis', y_axis_label='Y-axis')
p.line([1, 2, 3, 4, 5], [10, 15, 13, 17, 19], legend_label='Trend', line_width=2)

show(p)
```

### Summary

Each library has its strengths:

- **Matplotlib:** Great for static, customizable plots.
- **Plotly:** Ideal for interactive and web-based visualizations.
- **Seaborn:** Simplifies complex statistical plots.
- **Bokeh:** Best for interactive, high-performance visualizations.

To master data visualization, practice creating various types of plots and customize them to suit your needs. Combine these libraries to leverage their unique features and create comprehensive data visualizations.