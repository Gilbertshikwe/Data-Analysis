import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
tips = sns.load_dataset('tips')

# Exclude non-numeric columns for correlation calculation
numeric_columns = tips.select_dtypes(include=['float64', 'int64'])

# Scatter Plot
plt.figure()
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Scatter Plot of Total Bill vs Tip')
plt.savefig('scatter_plot.png')  # Save the plot
plt.close()

# Bar Plot
plt.figure()
sns.barplot(x='day', y='total_bill', data=tips)
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.title('Bar Plot of Total Bill by Day')
plt.savefig('bar_plot.png')  # Save the plot
plt.close()

# Histogram
plt.figure()
sns.histplot(tips['total_bill'], bins=30)
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.title('Histogram of Total Bill')
plt.savefig('histogram.png')  # Save the plot
plt.close()

# Box Plot
plt.figure()
sns.boxplot(x='day', y='total_bill', data=tips)
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.title('Box Plot of Total Bill by Day')
plt.savefig('box_plot.png')  # Save the plot
plt.close()

# Heatmap (using numeric columns)
plt.figure()
corr = numeric_columns.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Heatmap of Tips Dataset Correlation')
plt.savefig('heatmap.png')  # Save the plot
plt.close()
