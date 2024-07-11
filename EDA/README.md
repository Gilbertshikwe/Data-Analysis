# README

## Table of Contents
1. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
2. [Measures of Central Tendency](#measures-of-central-tendency)
3. [Measures of Spread](#measures-of-spread)
4. [Interquartile Range (IQR) and Quartile Deviation](#interquartile-range-iqr-and-quartile-deviation)
5. [ANOVA (Analysis of Variance)](#anova-analysis-of-variance)
6. [Skewness](#skewness)
7. [Kurtosis](#kurtosis)
8. [Calculating Skewness and Kurtosis in Python](#calculating-skewness-and-kurtosis-in-python)
9. [Difference Between Skewness and Kurtosis](#difference-between-skewness-and-kurtosis)

## Exploratory Data Analysis (EDA)
Exploratory Data Analysis is the process of examining and visualizing data to summarize its main characteristics. It includes understanding the data distribution, detecting outliers, and identifying patterns and relationships between variables.

### Univariate Data Analysis
Analysis of a single variable. Techniques include histograms, box plots, and summary statistics like mean, median, and mode.

### Bivariate Data Analysis
Analysis involving two variables to determine if there is any relationship between them. Techniques include scatter plots, correlation analysis, and joint distributions.

### Multivariate Data Analysis
Analysis involving more than two variables to understand complex relationships. Techniques include heatmaps, pair plots, and clustering methods.

## Measures of Central Tendency
These are statistics that describe the center of a data set.

### Mean
Average of all values in the data set.

### Median
Middle value in a sorted, ascending or descending, list of values.

### Mode
Most frequent value in the data set.

## Measures of Spread
These statistics describe how data is spread out from the center.

### Range
Difference between the maximum and minimum values in the data set.

### Variance
Average of the squared differences from the Mean.

### Standard Deviation
Square root of the variance, indicating the average amount of deviation from the mean.

## Interquartile Range (IQR) and Quartile Deviation
### Interquartile Range
Range of the middle 50% of the data, calculated as Q3 (75th percentile) minus Q1 (25th percentile).

### Quartile Deviation
Half of the Interquartile Range, providing a measure of dispersion around the median.

## ANOVA (Analysis of Variance)
ANOVA is a statistical method used to analyze whether there are significant differences between the means of two or more groups.

## Skewness
Skewness measures the asymmetry of the probability distribution of a real-valued random variable.

## Kurtosis
Kurtosis measures the "tailedness" of the probability distribution of a real-valued random variable.

## Calculating Skewness and Kurtosis in Python
You can use libraries like `scipy.stats` to calculate skewness and kurtosis in Python:

```python
import numpy as np
from scipy.stats import skew, kurtosis

# Example data
data = np.array([1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8])

# Calculate skewness
skewness = skew(data)
print("Skewness:", skewness)

# Calculate kurtosis
kurt = kurtosis(data)
print("Kurtosis:", kurt)
```

## Difference Between Skewness and Kurtosis
### Skewness
Measures the symmetry of the data distribution. A skewness of 0 indicates a perfectly symmetrical distribution.

### Kurtosis
Measures the heaviness of the tails or the peakness of the data distribution. A kurtosis of 3 (normal distribution) indicates a mesokurtic distribution. Values greater than 3 indicate leptokurtic (heavy-tailed) distributions, and values less than 3 indicate platykurtic (light-tailed) distributions.

Understanding these concepts will help you analyze data effectively, identify patterns, and make informed decisions in data-driven tasks. Let me know if you have any specific questions or if there's anything else you'd like to explore further!