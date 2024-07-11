import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #type:ignore
import seaborn as sns #type:ignore

def main():
    # Creating Data Structures

    # Series
    data = [1, 2, 3, 4, 5]
    series = pd.Series(data)
    print("Series:")
    print(series)
    print()

    # DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']
    }
    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)
    print()

    # Reading Data (using sample data as reading from files require actual files)
    print("Sample DataFrame (acting as read data):")
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
        'Age': [25, 30, 35, 25, 30],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'New York', 'San Francisco'],
        'Salary': [50000, 60000, 70000, 50000, 60000]
    })
    print(df)
    print()

    # Data Inspection
    print("First few rows of the DataFrame:")
    print(df.head())
    print()

    print("Summary statistics of the DataFrame:")
    print(df.describe())
    print()

    print("Information about the DataFrame:")
    print(df.info())
    print()

    # Data Manipulation
    print("Selecting the 'Age' column:")
    ages = df['Age']
    print(ages)
    print()

    print("Filtering rows where 'Age' > 25:")
    filtered_df = df[df['Age'] > 25]
    print(filtered_df)
    print()

    print("Adding a new column 'Experience' with dummy values:")
    df['Experience'] = [2, 5, 8, 2, 5]
    print(df)
    print()

    print("Dropping the 'Experience' column:")
    df = df.drop('Experience', axis=1)
    print(df)
    print()

    # Data Aggregation and Grouping
    print("Grouping by 'Name' and calculating the mean of numeric columns:")
    grouped_df = df.groupby('Name').mean(numeric_only=True)
    print(grouped_df)
    print()

    # Reading from CSV file
    print("Reading from CSV file:")
    csv_df = pd.read_csv('/home/gilbert/MyCodes/DataScience data/Spotify2024.csv', encoding='latin1')
    print(csv_df)
    print()

    # Writing to CSV file
    print("Writing DataFrame to CSV file:")
    csv_df.to_csv('output.csv', index=False)
    print("DataFrame successfully written to 'output.csv'")
    print()

    # Reading from Excel file
    print("Reading from Excel file:")
    excel_df = pd.read_excel('/home/gilbert/MyCodes/DataScience data/sample-superstore.xls', sheet_name='Orders')
    print(excel_df)
    print()

    # Writing to Excel file
    print("Writing DataFrame to Excel file:")
    excel_df.to_excel('output.xlsx', sheet_name='Orders', index=False)
    print("DataFrame successfully written to 'output.xlsx'")
    print()

     # Merging DataFrames
    print("Merging DataFrames:")
    sales_2023 = pd.DataFrame({
        'product_id': [101, 102, 103, 104],
        'sales_2023': [250, 150, 100, 200]
    })
    sales_2024 = pd.DataFrame({
        'product_id': [102, 104, 105, 106],
        'sales_2024': [300, 200, 150, 100]
    })
    merged_sales = pd.merge(sales_2023, sales_2024, on='product_id', how='inner')
    print(merged_sales)
    print()

    # Joining DataFrames
    print("Joining DataFrames:")
    employee_info = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie'],
        'department': ['HR', 'Engineering', 'Marketing']
    }, index=['E1', 'E2', 'E3'])
    employee_salary = pd.DataFrame({
        'salary': [70000, 80000, 90000],
        'bonus': [5000, 10000, 7000]
    }, index=['E1', 'E3', 'E4'])
    joined_employee_data = employee_info.join(employee_salary, how='inner')
    print(joined_employee_data)
    print()

    # Concatenating DataFrames
    print("Concatenating DataFrames:")
    q1_sales = pd.DataFrame({
        'product_id': [101, 102, 103],
        'q1_sales': [100, 150, 200]
    })
    q2_sales = pd.DataFrame({
        'product_id': [101, 102, 103],
        'q2_sales': [120, 130, 220]
    })
    concatenated_sales = pd.concat([q1_sales, q2_sales], axis=1)
    print(concatenated_sales)
    print()

    # Comparing DataFrames
    print("Comparing DataFrames:")
    sales_data_2023 = pd.DataFrame({
        'product_id': [101, 102, 103],
        'sales': [250, 150, 100]
    })
    sales_data_2024 = pd.DataFrame({
        'product_id': [101, 102, 103],
        'sales': [260, 155, 110]
    })
    comparison_sales = sales_data_2023.compare(sales_data_2024)
    print(comparison_sales)
    print()

    # Data Visualization
    print("Data Visualization Examples:")

    # Sample data for visualization
    viz_data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E'],
        'Values1': [23, 48, 12, 35, 19],
        'Values2': [15, 30, 20, 25, 10],
        'Values3': [50, 40, 45, 35, 55]
    })

    # Bar plot using matplotlib
    plt.figure(figsize=(10, 5))
    plt.bar(viz_data['Category'], viz_data['Values1'])
    plt.title('Bar Plot of Values1 by Category')
    plt.xlabel('Category')
    plt.ylabel('Values1')
    plt.savefig('bar_plot.png')
    plt.close()
    print("Bar plot saved as 'bar_plot.png'")

    # Line plot using matplotlib
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
    print("Line plot saved as 'line_plot.png'")

    # Scatter plot using seaborn
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=viz_data.melt(id_vars=['Category'], var_name='Variable', value_name='Value'), 
                    x='Category', y='Value', hue='Variable')
    plt.title('Scatter Plot of Values by Category')
    plt.savefig('scatter_plot.png')
    plt.close()
    print("Scatter plot saved as 'scatter_plot.png'")

    # Heatmap using seaborn
    numeric_data = viz_data.select_dtypes(include=[np.number])
    correlation_matrix = numeric_data.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.savefig('heatmap.png')
    plt.close()
    print("Heatmap saved as 'heatmap.png'")

    # Box plot using seaborn
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=viz_data.melt(id_vars=['Category'], var_name='Variable', value_name='Value'), 
                x='Category', y='Value', hue='Variable')
    plt.title('Box Plot of Values by Category')
    plt.savefig('box_plot.png')
    plt.close()
    print("Box plot saved as 'box_plot.png'")

    # Visualization using data from previous examples
    # Histogram of Ages
    plt.figure(figsize=(10, 5))
    df['Age'].hist(bins=10)
    plt.title('Histogram of Ages')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.savefig('age_histogram.png')
    plt.close()
    print("Age histogram saved as 'age_histogram.png'")

    # Scatter plot of Age vs Salary
    plt.figure(figsize=(10, 5))
    plt.scatter(df['Age'], df['Salary'])
    plt.title('Age vs Salary')
    plt.xlabel('Age')
    plt.ylabel('Salary')
    plt.savefig('age_salary_scatter.png')
    plt.close()
    print("Age vs Salary scatter plot saved as 'age_salary_scatter.png'")

if __name__ == "__main__":
    main()

