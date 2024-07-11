import pandas as pd
import numpy as np

# Step 1: Loading the Dataset
file_path = '/home/gilbert/MyCodes/DataScience data/titanic.csv'  # Replace with actual path
df = pd.read_csv(file_path)

# Step 2: Inspecting the Data
print("Step 2: Inspecting the Data")
print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()

# Step 3: Handling Missing Values
print("Step 3: Handling Missing Values")

# Check for missing values
print("Missing values before handling:")
print(df.isnull().sum())
print()

# Handling missing values
# Fill missing Age values with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill missing Embarked values with the most frequent value (mode)
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop Cabin column due to a high number of missing values
df = df.drop(columns=['Cabin'])

# Check for missing values after handling
print("Missing values after handling:")
print(df.isnull().sum())
print()

# Step 4: Removing Duplicates
print("Step 4: Removing Duplicates")

# Check for duplicates
print("Duplicates before removing:")
print(df.duplicated().sum())
print()

# Remove duplicates
df = df.drop_duplicates()

# Check for duplicates after removing
print("Duplicates after removing:")
print(df.duplicated().sum())
print()

# Step 5: Correcting Errors
print("Step 5: Correcting Errors")

# Check for unique values in categorical columns
print("Unique values in Embarked column:")
print(df['Embarked'].unique())
print()

# Correct any incorrect values if found (in this case, there are no incorrect values)

# Step 6: Ensuring Consistency
print("Step 6: Ensuring Consistency")

# Convert all categorical columns to consistent format (e.g., title case)
df['Name'] = df['Name'].str.title()
df['Sex'] = df['Sex'].str.lower()
df['Embarked'] = df['Embarked'].str.upper()

print("Data after ensuring consistency:")
print(df.head())
print()

# Optionally, you can save the cleaned data to a new CSV file
df.to_csv('/home/gilbert/MyCodes/DataScience data/cleaned_titanic.csv', index=False)
