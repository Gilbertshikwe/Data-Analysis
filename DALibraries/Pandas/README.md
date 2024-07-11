# Pandas Library in Python

## Introduction

Pandas is a powerful, open-source data analysis and data manipulation library for Python. It provides data structures and functions needed to efficiently manipulate large datasets, making it an essential tool for data scientists and analysts.

## Features of Pandas

- **Data Structures**: Pandas introduces two primary data structures - Series (1-dimensional) and DataFrame (2-dimensional), which allow for the efficient manipulation of data.
- **Data Cleaning**: Easy handling of missing data, data alignment, and data transformation.
- **Data Wrangling**: Powerful group by functionality, merging, and joining datasets.
- **Data Analysis**: Provides tools for filtering, grouping, and aggregation.
- **Input/Output**: Supports reading from and writing to various file formats (CSV, Excel, SQL, JSON, etc.).
- **Time Series**: Provides robust tools for working with time series data, including date range generation and frequency conversion.

## Installation

To install Pandas, you can use pip, the Python package manager. Run the following command in your terminal:

```sh
pip install pandas
```

## Basic Usage

### Importing Pandas

To start using Pandas, you need to import it into your Python script:

```python
import pandas as pd
```

### Creating Data Structures

#### Series

A Pandas Series is a one-dimensional array-like object that can hold any data type:

```python
import pandas as pd

data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)
```

#### DataFrame

A Pandas DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns):

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)
print(df)
```

### Data Operations

#### Reading Data

Pandas supports reading data from various file formats:

```python
import pandas as pd

# Reading data from a CSV file
df = pd.read_csv('data.csv')

# Reading data from an Excel file
df = pd.read_excel('data.xlsx')

# Reading data from a JSON file
df = pd.read_json('data.json')
```

#### Data Inspection

You can inspect your DataFrame using several methods:

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)

# Display the first few rows
print(df.head())

# Display summary statistics
print(df.describe())

# Display information about the DataFrame
print(df.info())
```

#### Data Manipulation

Pandas provides various methods for data manipulation:

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)

# Selecting a column
ages = df['Age']
print(ages)

# Filtering rows
filtered_df = df[df['Age'] > 25]
print(filtered_df)

# Adding a new column
df['Salary'] = [50000, 60000, 70000]
print(df)

# Dropping a column
df = df.drop('Salary', axis=1)
print(df)
```

### Data Aggregation and Grouping

Pandas makes it easy to group data and perform aggregation operations:

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
    'Age': [25, 30, 35, 25, 30],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'New York', 'San Francisco'],
    'Salary': [50000, 60000, 70000, 50000, 60000]
}
df = pd.DataFrame(data)

# Grouping data by a column and calculating the mean
grouped_df = df.groupby('Name').mean()
print(grouped_df)
```
# Working with CSV Files and Excel Files Using Pandas

Pandas is a powerful Python library for data manipulation and analysis. It provides easy-to-use data structures and tools for reading, writing, and manipulating data from various sources, including CSV files and Excel files.

## Table of Contents

1. [Reading CSV Files](#reading-csv-files)
2. [Writing to CSV Files](#writing-to-csv-files)
3. [Reading Excel Files](#reading-excel-files)
4. [Writing to Excel Files](#writing-to-excel-files)
5. [Additional Operations](#additional-operations)

---

### Reading CSV Files

To read data from a CSV file into a Pandas DataFrame:

```python
import pandas as pd

# Reading a CSV file into a DataFrame
df = pd.read_csv('data.csv')
```

Replace `'data.csv'` with the path to your CSV file. Pandas automatically detects the headers (column names) from the first row of the CSV file.

### Writing to CSV Files

To write data from a Pandas DataFrame back to a CSV file:

```python
# Writing DataFrame to a CSV file
df.to_csv('output.csv', index=False)
```

Replace `'output.csv'` with the desired name and path for the output CSV file. The `index=False` parameter ensures that the index (row numbers) are not written to the CSV file.

### Reading Excel Files

To read data from an Excel file into a Pandas DataFrame:

```python
# Reading an Excel file into a DataFrame
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
```

Replace `'data.xlsx'` with the path to your Excel file. Specify the `sheet_name` parameter with the name of the sheet you want to read from. If not specified, Pandas reads the first sheet by default.

### Writing to Excel Files

To write data from a Pandas DataFrame back to an Excel file:

```python
# Writing DataFrame to an Excel file
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)
```

Replace `'output.xlsx'` with the desired name and path for the output Excel file. The `sheet_name` parameter specifies the sheet name for the output. The `index=False` parameter prevents writing the index (row numbers) to the Excel file.

### Additional Operations

Pandas offers a wide range of operations for manipulating DataFrames:

- **Manipulating DataFrames:** Selecting columns, filtering rows, aggregating data, merging/joining DataFrames, and more.
  
- **Handling Missing Data:** Methods like `dropna()` and `fillna()` to handle missing data efficiently.
  
- **Data Transformation:** Sorting, grouping, applying functions row-wise or column-wise.
  
- **Advanced Operations:** Pivot tables, hierarchical indexing, reshaping data.

# Pandas DataFrame Operations

This repository contains a Python script that demonstrates how to perform various operations on Pandas DataFrames, including merging, joining, concatenating, and comparing DataFrames.

## Requirements

To run the script, you need to have the following Python libraries installed:

- pandas

You can install the required dependencies using pip:

```bash
pip install pandas
```

## Script Overview

The script (`panda.py`) includes examples of the following operations:

1. **Merging DataFrames**
2. **Joining DataFrames**
3. **Concatenating DataFrames**
4. **Comparing DataFrames**

### 1. Merging DataFrames

The script demonstrates how to merge two DataFrames using the `pd.merge()` function. The `how` parameter specifies the type of merge to be performed. In this example, an inner merge is used.

```python
import pandas as pd

df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'key': ['B', 'D', 'E', 'F'],
    'value': [5, 6, 7, 8]
})

merged_df = pd.merge(df1, df2, on='key', how='inner')
print(merged_df)
```

### 2. Joining DataFrames

The script shows how to join two DataFrames using the `df.join()` method. The `how` parameter specifies the join method to be used. In this example, an inner join is performed.

```python
df3 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
}, index=['K0', 'K1', 'K2'])

df4 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2']
}, index=['K0', 'K2', 'K3'])

joined_df = df3.join(df4, how='inner')
print(joined_df)
```

### 3. Concatenating DataFrames

The script demonstrates how to concatenate two DataFrames along the columns using the `pd.concat()` function with `axis=1`.

```python
df5 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

df6 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

concatenated_df = pd.concat([df5, df6], axis=1)
print(concatenated_df)
```

### 4. Comparing DataFrames

The script demonstrates how to compare two DataFrames using the `df.compare()` method to highlight the differences between them.

```python
df7 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

df8 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A4'],
    'B': ['B0', 'B1', 'B2', 'B4']
})

comparison_df = df7.compare(df8)
print(comparison_df)
```

## Running the Script

To run the script, execute the following command in your terminal:

```bash
python panda.py
```

The script will print the results of each operation to the console, demonstrating how to perform merging, joining, concatenating, and comparing DataFrames using Pandas.

# Data Visualization Examples

This repository provides a set of examples demonstrating various data visualization techniques using Python libraries such as Matplotlib and Seaborn. The sample data used in these examples represents different categories and their corresponding values. The visualizations include bar plots, line plots, scatter plots, heatmaps, box plots, histograms, and scatter plots for different datasets.

## Sample Data

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample data for visualization
viz_data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values1': [23, 48, 12, 35, 19],
    'Values2': [15, 30, 20, 25, 10],
    'Values3': [50, 40, 45, 35, 55]
})
```

## Visualizations

### 1. Bar Plot

A bar plot is created to visualize the 'Values1' by 'Category'.

```python
plt.figure(figsize=(10, 5))
plt.bar(viz_data['Category'], viz_data['Values1'])
plt.title('Bar Plot of Values1 by Category')
plt.xlabel('Category')
plt.ylabel('Values1')
plt.savefig('bar_plot.png')
plt.close()
```

![Bar Plot](bar_plot.png)

### 2. Line Plot

A line plot is created to visualize 'Values1', 'Values2', and 'Values3' by 'Category'.

```python
plt.figure(figsize=(10, 5))
plt.plot(viz_data['Category'], viz_data['Values1'], marker='o', label='Values1')
plt.plot(viz_data['Category'], viz_data['Values2'], marker='s', label='Values2')
plt.plot(viz_data['Category'], viz_data['Values3'], marker='^', label='Values3')
plt.title('Line Plot of Values by Category')
plt.xlabel('Category')
plt.ylabel('Values')
plt.legend()
plt.savefig('line_plot.png')
plt.close()
```

![Line Plot](line_plot.png)

### 3. Scatter Plot

A scatter plot is created to visualize the distribution of 'Values1', 'Values2', and 'Values3' by 'Category'.

```python
plt.figure(figsize=(10, 5))
sns.scatterplot(data=viz_data.melt(id_vars=['Category'], var_name='Variable', value_name='Value'), 
                x='Category', y='Value', hue='Variable')
plt.title('Scatter Plot of Values by Category')
plt.savefig('scatter_plot.png')
plt.close()
```

![Scatter Plot](scatter_plot.png)

### 4. Heatmap

A heatmap is created to visualize the correlation between 'Values1', 'Values2', and 'Values3'.

```python
numeric_data = viz_data.select_dtypes(include=[np.number])
correlation_matrix = numeric_data.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('heatmap.png')
plt.close()
```

![Heatmap](heatmap.png)

### 5. Box Plot

A box plot is created to visualize the distribution of 'Values1', 'Values2', and 'Values3' by 'Category'.

```python
plt.figure(figsize=(12, 6))
sns.boxplot(data=viz_data.melt(id_vars=['Category'], var_name='Variable', value_name='Value'), 
            x='Category', y='Value', hue='Variable')
plt.title('Box Plot of Values by Category')
plt.savefig('box_plot.png')
plt.close()
```

![Box Plot](box_plot.png)

## Additional Visualizations

### 6. Histogram of Ages

A histogram is created to visualize the distribution of ages from a different dataset.

```python
plt.figure(figsize=(10, 5))
df['Age'].hist(bins=10)
plt.title('Histogram of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('age_histogram.png')
plt.close()
```

![Age Histogram](age_histogram.png)

### 7. Scatter Plot of Age vs Salary

A scatter plot is created to visualize the relationship between age and salary from a different dataset.

```python
plt.figure(figsize=(10, 5))
plt.scatter(df['Age'], df['Salary'])
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.savefig('age_salary_scatter.png')
plt.close()
```

![Age vs Salary Scatter Plot](age_salary_scatter.png)

## Conclusion

These examples illustrate various data visualization techniques using Matplotlib and Seaborn. Each visualization provides insights into the data and helps in understanding the underlying patterns and relationships. Feel free to explore and modify the code to suit your data visualization needs.

## Conclusion

Pandas is an essential library for data analysis and manipulation in Python. Its powerful data structures and wide range of functions make it an indispensable tool for data scientists and analysts. By learning to use Pandas effectively, you can streamline your data processing workflows and gain deeper insights from your data.

For more detailed documentation and tutorials, visit the official [Pandas documentation](https://pandas.pydata.org/).