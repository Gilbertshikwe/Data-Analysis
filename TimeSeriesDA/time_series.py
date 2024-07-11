import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Load the dataset
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv'
df = pd.read_csv(url, index_col='Month', parse_dates=True)
df.index.freq = 'MS'  # Set the frequency to monthly start

# Display the first few rows
print("Dataset:")
print(df.head())
print()

# Plot the time series
plt.figure(figsize=(12, 6))
plt.plot(df, label='Passengers')
plt.title('Monthly Airline Passengers')
plt.xlabel('Date')
plt.ylabel('Number of Passengers')
plt.legend()
plt.savefig('time_series_plot.png')
plt.close()

# Decompose the time series
decomposition = seasonal_decompose(df['Passengers'], model='multiplicative')
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

plt.figure(figsize=(12, 8))
plt.subplot(411)
plt.plot(df['Passengers'], label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(seasonal, label='Seasonality')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(residual, label='Residuals')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('decomposition.png')
plt.close()

# Check for stationarity with the Augmented Dickey-Fuller test
result = adfuller(df['Passengers'])
print("ADF Statistic:", result[0])
print("p-value:", result[1])
for key, value in result[4].items():
    print('Critical Values:')
    print(f'   {key}, {value}')

# Differencing to make the series stationary
df['Passengers_diff'] = df['Passengers'] - df['Passengers'].shift(1)
df['Passengers_diff'].dropna().plot(figsize=(12, 6))
plt.title('Differenced Series')
plt.savefig('differenced_series.png')
plt.close()

# Fit ARIMA model
model = ARIMA(df['Passengers'], order=(1, 1, 1))
model_fit = model.fit()
print(model_fit.summary())

# Forecast
forecast = model_fit.forecast(steps=12)
forecast_series = pd.Series(forecast, index=pd.date_range(start='1961-01-01', periods=12, freq='MS'))

plt.figure(figsize=(12, 6))
plt.plot(df['Passengers'], label='Original')
plt.plot(forecast_series, label='Forecast', color='red')
plt.title('Forecasted Passengers')
plt.xlabel('Date')
plt.ylabel('Number of Passengers')
plt.legend()
plt.savefig('forecast.png')
plt.close()