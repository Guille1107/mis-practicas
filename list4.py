inventario = ["laptop","tarjeta de video","procesador","memoria RAM"]
inventario.append("disco SSD")
inventario.insert(2 ,"fuente de poder")
inventario.extend(["gabinete","monitor 4K","teclado mecanico","mouse gamer"])
if "monitor 4K" in inventario:
    print("monitor 4K encontrado en la posicion: ", inventario.index("monitor 4K"))
inventario[inventario.index("memoria RAM")] = "memoria RAM DDR5"
equipo_despachado = inventario.pop()
inventario.remove("tarjeta de video")

print("Producto extraido: ", equipo_despachado)
print("Inventario final: ",inventario)
print("Cantidad total de componentes: ",len (inventario))
