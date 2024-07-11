import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
from scipy.stats import skew, kurtosis, f_oneway
from sklearn.cluster import KMeans

# Generate example data
np.random.seed(0)
data_univariate = np.random.normal(loc=0, scale=1, size=1000)
data_bivariate_x = np.random.normal(loc=0, scale=1, size=100)
data_bivariate_y = 2 * data_bivariate_x + np.random.normal(loc=0, scale=1, size=100)
iris = sns.load_dataset('iris')

# Univariate Data Analysis
plt.figure(figsize=(10, 6))
plt.hist(data_univariate, bins=30)
plt.title('Histogram (Univariate)')
plt.savefig('histogram_univariate.png')
plt.close()

mean = np.mean(data_univariate)
median = np.median(data_univariate)
mode = float(stats.mode(data_univariate)[0])
print(f"Mean: {mean}, Median: {median}, Mode: {mode}")

# Bivariate Data Analysis
plt.figure(figsize=(10, 6))
plt.scatter(data_bivariate_x, data_bivariate_y)
plt.title('Scatter Plot (Bivariate)')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('scatter_bivariate.png')
plt.close()

correlation = np.corrcoef(data_bivariate_x, data_bivariate_y)[0, 1]
print(f"Correlation coefficient: {correlation}")

# Multivariate Data Analysis
sns.pairplot(iris, hue='species')
plt.suptitle('Pair Plot (Multivariate)', y=1.02)
plt.savefig('pairplot_multivariate.png')
plt.close()

X = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
iris['cluster'] = kmeans.labels_
print("Cluster centers:")
print(kmeans.cluster_centers_)

# Measures of Central Tendency
mean = np.mean(data_univariate)
median = np.median(data_univariate)
mode = float(stats.mode(data_univariate)[0])
print(f"Mean: {mean}, Median: {median}, Mode: {mode}")

# Measures of Spread
data_range = np.max(data_univariate) - np.min(data_univariate)
variance = np.var(data_univariate)
std_deviation = np.std(data_univariate)
print(f"Range: {data_range}, Variance: {variance}, Standard Deviation: {std_deviation}")

# Interquartile Range and Quartile Deviation
q75, q25 = np.percentile(data_univariate, [75, 25])
iqr = q75 - q25
quartile_deviation = iqr / 2
print(f"IQR: {iqr}, Quartile Deviation: {quartile_deviation}")

# ANOVA (Analysis of Variance)
group1 = [18, 20, 16, 22, 19]
group2 = [23, 25, 27, 21, 24]
group3 = [17, 16, 18, 21, 19]
f_statistic, p_value = stats.f_oneway(group1, group2, group3)
print(f"F-statistic: {f_statistic}, p-value: {p_value}")

# Skewness and Kurtosis
skewness = skew(data_univariate)
kurt = kurtosis(data_univariate)
print(f"Skewness: {skewness}, Kurtosis: {kurt}")
