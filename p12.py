from math import ceil
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

def lowess(x, y, f, iterations):
    n = len(x)
    r = int(ceil(f * n))
    h = np.array([np.sort(np.abs(x - xi))[r] for xi in x])
    w = np.clip(np.abs((x[:, None] - x[None, :]) / h), 0.0, 1.0)
    w = (1 - w ** 3) ** 3
    yest = np.zeros(n)
    delta = np.ones(n)
    
    for iteration in range(iterations):
        for i in range(n):
            weights = delta * w[:, i]
            b = np.array([np.sum(weights * y), np.sum(weights * y * x)])
            A = np.array([[np.sum(weights), np.sum(weights * x)],
                          [np.sum(weights * x), np.sum(weights * x * x)]])
            beta = linalg.solve(A, b)
            yest[i] = beta[0] + beta[1] * x[i]

        residuals = y - yest
        s = np.median(np.abs(residuals))
        delta = np.clip(residuals / (6.0 * s), -1, 1)
        delta = (1 - delta ** 2) ** 2

    return yest

n = 100
x = np.linspace(0, 2 * np.pi, n)
y = np.sin(x) + 0.3 * np.random.randn(n)
f = 0.25
iterations = 3

yest = lowess(x, y, f, iterations)

plt.figure(figsize=(10, 6))
plt.plot(x, y, "r.", label='Data')
plt.plot(x, yest, "b-", label='Lowess Smoothing')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lowess Smoothing')
plt.legend()
plt.show()
