import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Suma elemento a elemento
suma = A + B
print("..Suma(A+B)..")
print(suma)
print() # Imprime una línea en blanco para separar

prod_elem = A * B
print("..MULTIPLICACIÓN ELEMENTO A ELEMENTO (A*B)..")
print(prod_elem)
print()

#Producto matricial
prod_mat = A@B
print("..Producción matricial(A@B)..")
print(prod_mat)
print()

#Transpuesta
transpuesta= A.T
print("..Transpuesta de A.T..")
print(transpuesta)
print()

#Determinante e inversa
det=np.linalg.det(A)
inv=np.linalg.det(B)
print("..Determinante de A..")
print(det)
print("..Determinante de B..")
print(inv)