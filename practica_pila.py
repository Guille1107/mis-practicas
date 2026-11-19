pila = []

for i in range(1, 11):
    pila.append("Camisa " + str(i))

print("Pila con 10 camisas:")
print(pila)

print("\nElemento en la cima:")
print(pila[-1])

print("\nRetirando 4 camisas:")
for i in range(4):
    print("Se retiró:", pila.pop())

print("\nTamaño de la pila:", len(pila))

if len(pila) == 0:
    print("La pila está vacía")
else:
    print("La pila no está vacía")

print("\nVaciando la pila:")
while len(pila) > 0:
    print("Se retiró:", pila.pop())

print("Pila final:", pila)
print("Tamaño final:", len(pila))

if len(pila) == 0:
    print("La pila está vacía")
else:
    print("La pila no está vacía")