import matplotlib.pyplot as plt
import numpy as np

#створюємо масив значень x від 1 до 10 з достатньою кількістю точок для плавного графіка.
x = np.linspace(1, 10, 1000)

#обчислюємо значення функції Y(x).
Y = 5 * np.sin(x) * np.cos(x**2 + 1/x)**2

#побудова графіка.
plt.plot(x, Y, label='\(5 \cdot \sin(x) \cdot \cos(x^2 + \frac{1}{x})^2\)', color='red', linewidth=2)

#налаштування заголовку та підписів осей.
plt.title('Графік функції \(Y(x)\)', fontsize=15)
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('Y', fontsize=12, color='blue')

#додавання легенди.
plt.legend()

#додавання сітки.
plt.grid(True)

#відображення графіка.
plt.show()