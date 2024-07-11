import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values
data = {
    'Car': ['Toyota', 'Honda', 'Ford', np.nan, 'Nissan'],
    'Price': [25000, 30000, np.nan, 22000, 28000],
    'Mileage': [np.nan, 40000, 60000, 35000, 50000],
    'Color': ['Red', 'Blue', 'Black', 'White', np.nan]
}

df = pd.DataFrame(data)

# Display the DataFrame with missing values
print("Original DataFrame:")
print(df)
print()

# Method 1: Dropping missing values
df_dropped = df.dropna()
print("DataFrame after dropping rows with any missing values:")
print(df_dropped)
print()

# Method 2: Filling missing values with a specific value
df_filled = df.fillna(value='Unknown')
print("DataFrame after filling missing values with 'Unknown':")
print(df_filled)
print()

# Method 3: Filling missing values with mean of each numeric column
df_mean_filled = df.copy()
df_mean_filled['Price'] = df_mean_filled['Price'].fillna(df['Price'].mean())
df_mean_filled['Mileage'] = df_mean_filled['Mileage'].fillna(df['Mileage'].mean())
print("DataFrame after filling missing numeric values with mean of each column:")
print(df_mean_filled)
print()

# Method 4: Forward fill missing values for categorical data
df_ffill = df.ffill()
print("DataFrame after forward filling missing values:")
print(df_ffill)
print()

# Method 5: Backward fill missing values for categorical data
df_bfill = df.bfill()
print("DataFrame after backward filling missing values:")
print(df_bfill)
print()

# Method 6: Interpolate missing values
df_interpolated = df.copy()
# Interpolate numeric columns
df_interpolated[['Price', 'Mileage']] = df_interpolated[['Price', 'Mileage']].interpolate()
# Forward fill for object columns
df_interpolated[['Car', 'Color']] = df_interpolated[['Car', 'Color']].ffill().bfill()

print("DataFrame after interpolating missing values:")
print(df_interpolated)
print()

