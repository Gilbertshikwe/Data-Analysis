import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Step 1: Loading the Dataset
file_path = '/home/gilbert/MyCodes/DataScience data/diabetes.csv'  # Replace with actual path
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("Step 1: Loading the Dataset")
print(df.head())
print()

# Step 2: Handling Missing Data
print("Step 2: Handling Missing Data")
print("Before handling missing data:")
print(df.isnull().sum())

# Impute missing values (e.g., using mean or median)
df['BMI'] = df['BMI'].fillna(df['BMI'].median())
df['Glucose'] = df['Glucose'].fillna(df['Glucose'].mean())

print("After handling missing data:")
print(df.isnull().sum())
print()

# Step 3: Handling Categorical Data
print("Step 3: Handling Categorical Data")
print("Before handling categorical data:")
print(df.head())

# Convert categorical variable into dummy/indicator variables
df = pd.get_dummies(df, columns=['Outcome'], drop_first=True)

print("After handling categorical data:")
print(df.head())
print()

# Step 4: Data Scaling and Normalization
print("Step 4: Data Scaling and Normalization")
print("Before scaling and normalization:")
print(df.head())

# Example: Standardization (Z-score normalization)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['Pregnancies', 'Glucose', 'BloodPressure']])
df[['Pregnancies', 'Glucose', 'BloodPressure']] = scaled_data

print("After scaling and normalization:")
print(df.head())
print()

# Step 5: Handling Outliers
print("Step 5: Handling Outliers")
print("Before handling outliers:")
print(df.describe())

# Detect outliers using Z-score
z_scores = np.abs(stats.zscore(df['BMI']))
outliers = (z_scores > 3)
df.loc[outliers, 'BMI'] = df['BMI'].median()

print("After handling outliers:")
print(df.describe())
print()

# Step 6: Feature Engineering
print("Step 6: Feature Engineering")
print("Before feature engineering:")
print(df.head())

# Example: Creating new feature (e.g., BMI category)
df['BMI_category'] = pd.cut(df['BMI'], bins=[0, 18.5, 24.9, 29.9, 100], labels=['Underweight', 'Normal', 'Overweight', 'Obese'])

print("After feature engineering:")
print(df.head())
print()

# Step 7: Splitting the Dataset
print("Step 7: Splitting the Dataset")

X = df.drop('Outcome_1', axis=1)  # Features
y = df['Outcome_1']  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print()

# Step 8: Data Integration and Transformation
print("Step 8: Data Integration and Transformation")
print("Before data integration and transformation:")
print(df.head())

# Ensure all values are positive and non-zero before log transformation
df['Glucose_log'] = np.log(df['Glucose'] + 1)  # Adding 1 to avoid log(0)

print("After data integration and transformation:")
print(df.head())
print()

# Optionally, you can save the preprocessed data to a new CSV file
df.to_csv('/home/gilbert/MyCodes/DataScience data/processed_diabetes.csv', index=False)

