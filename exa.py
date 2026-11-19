nombres = ["Ana","Carlos","Diana"]
print("---------------------------")
print("Lista Original")
print(nombres)

#Insercion
nombres.insert(1, "Beatriz")
print("---------------------------")
print("Primeros 3 estudiantes")
print(nombres[0:3])

print("---------------------------")
print(nombres[1:4])

# Agregando a Elena al final
nombres.append("Elena")
print("---------------------------")
print("Subgrupo del indice 1 al 3") 
# SOLUCIÓN: Cualquiera de estas tres opciones te dará ['Diana', 'Elena']
print(nombres[3:5]) 

print("---------------------------")
print(nombres[::-1])
