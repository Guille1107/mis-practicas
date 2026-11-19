def maxima_profundidad(comentarios: list)-> int:
    if not comentarios:
        return 0
    max_profundidad = 0
    for elemento in comentarios:
        if isinstance(elemento, list):
            profundidad_actual = 1 + maxima_profundidad(elemento)
        else:
            profundidad_actual = 1
        if profundidad_actual > max_profundidad:
            max_profundidad = profundidad_actual
    return max_profundidad

hilo = ["Comentario 1", ["Respuesta 1.1", ["Respuesta 1.1.1"]], "Comentario 2"]
print(maxima_profundidad(hilo))