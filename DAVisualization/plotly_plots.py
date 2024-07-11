import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px

# Enable offline mode
pio.renderers.default = "browser"

# Line Plot
fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4, 5], y=[10, 15, 13, 17, 19], mode='lines+markers'))
fig.update_layout(title='Line Plot', xaxis_title='X-axis', yaxis_title='Y-axis')
pio.write_html(fig, file='line_plot.html', auto_open=True)

# Bar Plot
categories = ['A', 'B', 'C', 'D', 'E']
values = [4, 7, 1, 8, 5]
fig = go.Figure(data=[go.Bar(x=categories, y=values)])
fig.update_layout(title='Bar Plot', xaxis_title='Categories', yaxis_title='Values')
pio.write_html(fig, file='bar_plot.html', auto_open=True)

# Scatter Plot
fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4, 5], y=[10, 15, 13, 17, 19], mode='markers'))
fig.update_layout(title='Scatter Plot', xaxis_title='X-axis', yaxis_title='Y-axis')
pio.write_html(fig, file='scatter_plot.html', auto_open=True)

# Histogram
data = [2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14]
fig = go.Figure(data=[go.Histogram(x=data)])
fig.update_layout(title='Histogram', xaxis_title='Value', yaxis_title='Frequency')
pio.write_html(fig, file='histogram.html', auto_open=True)

# Box Plot
fig = go.Figure(data=[go.Box(y=[2, 3, 4, 5, 6, 7, 8, 9, 10])])
fig.update_layout(title='Box Plot', xaxis_title='Category', yaxis_title='Value')
pio.write_html(fig, file='box_plot.html', auto_open=True)
