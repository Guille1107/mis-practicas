import numpy as np

A = np.array([[10, 15], [20, 5]])
B = np.array([[5, 12], [15, 8]])

total_ventas = A + B

precio = 50
ingreso_total = total_ventas * precio

print("Total de productos vendidos (Sábado + Domingo):")
print(total_ventas)

print("\nIngreso total en pesos (a 50 pesos por producto):")
print(ingreso_total)
