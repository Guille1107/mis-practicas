frutas = ["manzana","guayaba","uva"]
#ACTUALIZAR
frutas[1] = "pera"
#FRUTAS
frutas.append("sandia")
#UNE MULTIPLES ELEMENTOS AL FINAL DE LA LISTA
frutas.extend(["kiwi","mango"])
#ELIMINAR
retirado = frutas.pop(2)
ultimo=frutas.pop()
#BUSCA EL VALOR EXACTO Y ELIMINA LA PRIMERA APARICION
frutas.remove("sandia")
#DEL UTILIZA PALABRA CLAVE PARA BORRAR UNA CASILLA DIRECTAMENTE
del frutas[0]

posicion=frutas.index("kiwi")

#IMPRESION
print(frutas)