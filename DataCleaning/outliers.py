import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Create a sample DataFrame with some outliers
np.random.seed(42)
data = {
    'Age': np.random.randint(20, 60, 100),  # Age of individuals
    'Income': np.random.normal(50000, 10000, 100),  # Income in dollars
}
data['Income'][0] = 150000  # Introducing an outlier in income

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)
print()

# Method 1: Visualize outliers using box plot
plt.figure(figsize=(8, 6))
sns.boxplot(data=df)
plt.title('Boxplot of Age and Income')
plt.savefig('boxplot.png')  # Save the plot to a file
plt.close()  # Close the plot to release resources

# Method 2: Detect outliers using Z-score
z_scores = np.abs(stats.zscore(df))
threshold = 2.5  # Adjust threshold based on the dataset characteristics
outliers = np.where(z_scores > threshold)

print("Outliers detected using Z-score:")
for col, idx in zip(df.columns, outliers[0]):
    print(f"Column '{col}', Row '{idx}': Value {df.iloc[idx][col]}")

# Method 3: Remove outliers based on Z-score
df_cleaned = df[(z_scores < threshold).all(axis=1)]

print("\nDataFrame after removing outliers:")
print(df_cleaned)

