import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2
max_f = f(b)  # Максимальне значення f(x) в діапазоні [a, b]

# Кількість випадкових точок
N = 10000

# Генерація випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, max_f, N)

# Перевірка, скільки точок потрапляє під криву функції
under_curve = y_random < f(x_random)
estimate = np.sum(under_curve) / N * (b - a) * max_f

# Використання функції quad з бібліотеки scipy для порівняння
actual_integral, error = spi.quad(f, a, b)

# Побудова графіка функції та точок
plt.figure(figsize=(8, 6))
x = np.linspace(a, b, 1000)
plt.plot(x, f(x), 'r', label='f(x) = x^2')
plt.scatter(x_random, y_random, c=under_curve, cmap='winter', alpha=0.5, edgecolor='none')
plt.fill_between(x, f(x), color='gray', alpha=0.3)
plt.title('Інтегрування методом Монте-Карло та вибірка точок')
plt.legend()
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

# Виведення результатів
print(f"Оцінка інтегралу методом Монте-Карло: {estimate}")
print(f"Точне значення інтегралу (за допомогою quad): {actual_integral}")
print(f"Помилка в оцінці: {abs(estimate - actual_integral)}")
