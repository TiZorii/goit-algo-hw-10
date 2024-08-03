import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Function definition
def f(x):
    return x ** 2

# Integration bounds
a = 0
b = 2
max_f = f(b)  # The maximum value of f(x) in the range [a, b]

# Number of random points
N = 10000

# Generate random points
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, max_f, N)

# Check how many points fall below the function curve
under_curve = y_random < f(x_random)
estimate = np.sum(under_curve) / N * (b - a) * max_f

# Using scipy's quad function for comparison
actual_integral, error = spi.quad(f, a, b)

# Plotting the function and the points
plt.figure(figsize=(8, 6))
x = np.linspace(a, b, 1000)
plt.plot(x, f(x), 'r', label='f(x) = x^2')
plt.scatter(x_random, y_random, c=under_curve, cmap='winter', alpha=0.5, edgecolor='none')
plt.fill_between(x, f(x), color='gray', alpha=0.3)
plt.title('Monte Carlo Integration and Point Sampling')
plt.legend()
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

# Printing the results
print(f"Monte Carlo Estimate of Integral: {estimate}")
print(f"Actual Integral (using quad): {actual_integral}")
print(f"Error in Estimate: {abs(estimate - actual_integral)}")