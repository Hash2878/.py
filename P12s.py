import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Parameters
n = 100
degree = 3  # Degree of the polynomial
noise = 0.3

# Generate data
xpoints = np.linspace(0, 2 * math.pi, n).reshape(-1, 1)
ypoints = np.sin(xpoints) + noise * np.random.randn(n, 1)  # Add noise

# Polynomial transformation
poly = PolynomialFeatures(degree=degree)
x_poly = poly.fit_transform(xpoints)

# Fit polynomial regression model
linreg = LinearRegression()
linreg.fit(x_poly, ypoints)
prediction = linreg.predict(x_poly)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(xpoints, ypoints, color='red', label='Data')
plt.plot(xpoints, prediction, color='blue', label='Polynomial Regression Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Regression Fit')
plt.legend()
plt.show()
