historial_navegacion=[]
#Operación Apilar Push
historial_navegacion.append("google.com")
historial_navegacion.append("youtube.com")
historial_navegacion.append("wikipedia.org")
print("Historial cargado: ",historial_navegacion)
#Operación Top Peek
pagina_actual=historial_navegacion[-1]
print("Pagina actual en pantalla: ",pagina_actual)
#Operación para desapilar (Pop)
pagina_cerrada=historial_navegacion.pop()
print("saliendo de: ",pagina_cerrada)
print("historial despues de presionar 'atras'",historial_navegacion)

#Operación tamaño (size)
total_paginas=len(historial_navegacion)
print("paginas previas guardadas ",total_paginas)

#Operación vacia (Empty)
sin_paginas=len(historial_navegacion)==0
print("¿El historial esta vacio?",sin_paginas)
