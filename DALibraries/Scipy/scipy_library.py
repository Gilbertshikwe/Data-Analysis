import numpy as np
import scipy as sp
from scipy import stats, optimize, integrate, interpolate, linalg
import matplotlib.pyplot as plt

# Set the backend to a non-interactive one
plt.switch_backend('Agg')

# Descriptive Statistics
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("Skewness:", stats.skew(data))
print("Kurtosis:", stats.kurtosis(data))

# Probability Distributions
normal_samples = np.random.normal(loc=0, scale=1, size=1000)
mu, std = stats.norm.fit(normal_samples)
print("Mean:", mu, "Standard Deviation:", std)

plt.figure()
plt.hist(normal_samples, bins=30, density=True, alpha=0.6, color='g')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
plt.title("Normal Distribution")
plt.savefig('normal_distribution.png')
plt.close()

# Hypothesis Testing
t_statistic, p_value = stats.ttest_1samp(data, popmean=5)
print("T-statistic:", t_statistic, "P-value:", p_value)
data2 = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
t_statistic, p_value = stats.ttest_ind(data, data2)
print("T-statistic:", t_statistic, "P-value:", p_value)

t_statistic, p_value = stats.ttest_rel(data, data2)
print("T-statistic:", t_statistic, "P-value:", p_value)

# Optimization
def f(x):
    return x**2 + 5*np.sin(x)
result = optimize.minimize(f, x0=0)
print("Optimization Result:", result)

# Integration
def f(x):
    return x**2
result, error = integrate.quad(f, 0, 1)
print("Integral Result:", result, "Error:", error)

# Interpolation
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 9, 16, 25])
linear_interp = interpolate.interp1d(x, y)
x_new = np.linspace(0, 5, 50)
y_new = linear_interp(x_new)

plt.figure()
plt.plot(x, y, 'o', label='Original data')
plt.plot(x_new, y_new, '-', label='Linear interpolation')
plt.legend()
plt.savefig('linear_interpolation.png')
plt.close()

# Linear Algebra
A = np.array([[1, 2], [3, 4]])
A_inv = linalg.inv(A)
print("Inverse of A:\n", A_inv)
A_det = linalg.det(A)
print("Determinant of A:", A_det)
eigenvalues, eigenvectors = linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)



