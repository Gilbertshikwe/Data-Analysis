# README

## Table of Contents
1. [Introduction](#introduction)
2. [Key Concepts in Time Series Analysis](#key-concepts-in-time-series-analysis)
    1. [Time Series Components](#time-series-components)
    2. [Stationarity](#stationarity)
    3. [Autocorrelation](#autocorrelation)
3. [Steps in Time Series Analysis](#steps-in-time-series-analysis)
    1. [Loading and Visualizing Data](#loading-and-visualizing-data)
    2. [Preprocessing](#preprocessing)
    3. [Decomposition](#decomposition)
    4. [Modeling](#modeling)
    5. [Evaluation](#evaluation)
    6. [Forecasting](#forecasting)
4. [Example Analysis](#example-analysis)
    1. [Dataset](#dataset)
    2. [ADF Test Results](#adf-test-results)
    3. [SARIMAX Results](#sarimax-results)

## Introduction
Time series data analysis involves studying datasets collected over time. This type of analysis is crucial in various fields like finance, economics, and environmental science to forecast future values based on past trends.

## Key Concepts in Time Series Analysis

### Time Series Components

1. **Trend**: Long-term movement in the data.
2. **Seasonality**: Regular pattern repeating at regular intervals (e.g., monthly, quarterly).
3. **Cyclic**: Long-term oscillations without a fixed period, often influenced by economic or natural factors.
4. **Irregular**: Random or residual component that cannot be attributed to trend, seasonality, or cyclic patterns.

### Stationarity

A time series is said to be stationary if its statistical properties like mean, variance, and autocorrelation are constant over time. Stationarity is essential for many time series models.

### Autocorrelation

The correlation of a time series with its own past values. Autocorrelation plots (ACF and PACF) help in identifying the nature of the time series.

## Steps in Time Series Analysis

### 1. Loading and Visualizing Data

**Definition**: Load the data and perform initial visualizations to understand its structure and patterns.

**Example**:
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = 'path_to_titanic_csv_file/titanic.csv'  # Replace with actual path
df = pd.read_csv(file_path, index_col='Month', parse_dates=True)

# Display the first few rows of the dataset
print(df.head())

# Plot the data
df['Passengers'].plot(title='Monthly Number of Airline Passengers')
plt.show()
```

### 2. Preprocessing

**Definition**: Handle missing values, outliers, and perform necessary transformations like differencing to make the series stationary.

**Example**:
```python
# Check for missing values
print(df.isnull().sum())

# Handle missing values (if any)
df['Passengers'].fillna(df['Passengers'].median(), inplace=True)

# Differencing to make the series stationary
df_diff = df['Passengers'].diff().dropna()
```

### 3. Decomposition

**Definition**: Decompose the series into trend, seasonality, and residual components to understand underlying patterns.

**Example**:
```python
from statsmodels.tsa.seasonal import seasonal_decompose

# Decompose the time series
decomposition = seasonal_decompose(df['Passengers'], model='multiplicative')
decomposition.plot()
plt.show()
```

### 4. Modeling

**Definition**: Fit appropriate models like ARIMA, SARIMA, or Exponential Smoothing to the data.

**Example**:
```python
from statsmodels.tsa.arima.model import ARIMA

# Fit ARIMA model
model = ARIMA(df['Passengers'], order=(1, 1, 1))
model_fit = model.fit()

# Summary of the model
print(model_fit.summary())
```

### 5. Evaluation

**Definition**: Evaluate model performance using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and others.

**Example**:
```python
from sklearn.metrics import mean_squared_error

# Predict and evaluate
predictions = model_fit.predict(start=len(df)-12, end=len(df)-1, typ='levels')
actual = df['Passengers'][-12:]
mse = mean_squared_error(actual, predictions)
print(f'Mean Squared Error: {mse}')
```

### 6. Forecasting

**Definition**: Use the fitted model to forecast future values and validate the forecasts.

**Example**:
```python
# Forecast future values
forecast = model_fit.forecast(steps=12)
print(forecast)
```

## Example Analysis

### Dataset

```plaintext
            Passengers
Month                 
1949-01-01         112
1949-02-01         118
1949-03-01         132
1949-04-01         129
1949-05-01         121
```

### ADF Test Results

```plaintext
ADF Statistic: 0.8153688792060498
p-value: 0.991880243437641
Critical Values:
   1%, -3.4816817173418295
   5%, -2.8840418343195267
   10%, -2.578770059171598
```

**Interpretation**:
- The ADF statistic is 0.815, and the p-value is 0.992, which is higher than the typical significance levels (0.01, 0.05, 0.10).
- This suggests that the null hypothesis of the presence of a unit root cannot be rejected, indicating the time series is non-stationary.

### SARIMAX Results

```plaintext
                               SARIMAX Results                                
==============================================================================
Dep. Variable:             Passengers   No. Observations:                  144
Model:                 ARIMA(1, 1, 1)   Log Likelihood                -694.341
Date:                Thu, 11 Jul 2024   AIC                           1394.683
Time:                        10:56:41   BIC                           1403.571
Sample:                    01-01-1949   HQIC                          1398.294
                         - 12-01-1960                                         
Covariance Type:                  opg                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1         -0.4742      0.123     -3.847      0.000      -0.716      -0.233
ma.L1          0.8635      0.078     11.051      0.000       0.710       1.017
sigma2       961.9270    107.433      8.954      0.000     751.362    1172.492
===================================================================================
Ljung-Box (L1) (Q):                   0.21   Jarque-Bera (JB):                 2.14
Prob(Q):                              0.65   Prob(JB):                         0.34
Heteroskedasticity (H):               7.00   Skew:                            -0.21
Prob(H) (two-sided):                  0.00   Kurtosis:                         3.43
===================================================================================
```

**Interpretation**:
- The ARIMA(1,1,1) model has been fitted to the data.
- The coefficients for AR(1) and MA(1) terms are significant (p-values < 0.05).
- The Ljung-Box test indicates no significant autocorrelation in residuals (Prob(Q) = 0.65).
- Heteroskedasticity test indicates significant variability (Prob(H) = 0.00).

These results suggest that the ARIMA(1,1,1) model is an appropriate fit for this time series data, but further diagnostics and validation are necessary to ensure robust forecasting.

