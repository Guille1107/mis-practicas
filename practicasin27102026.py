A = [[10, 15], [20, 5]]
B = [[5, 12], [15, 8]]

total_ventas = [
    [A[i][j] + B[i][j] for j in range(2)]
    for i in range(2)
]

precio = 50

ingreso_total = [
    [total_ventas[i][j] * precio for j in range(2)]
    for i in range(2)
]

print("Total de productos vendidos (Sábado + Domingo):")
for fila in total_ventas:
    print(fila)

print("\nIngreso total en pesos (a 50 pesos por producto):")
for fila in ingreso_total:
    print(fila)
