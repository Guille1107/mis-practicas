def mostrar_encabezado_escuela():
    print("Instituto X")
    print("Registro y evaluación de calificaciones")


def obtener_nota_minima():
    return 6.0


def evaluar(nota_final):
    if nota_final <= 7.0:
        return "Reprobado"
    elif nota_final <= 9.4:
        return "Aprobado"
    else:
        return "Excelente"


def calcular_promedio(nota_examenes, nota_tareas):
    promedio = (nota_examenes * 0.70) + (nota_tareas * 0.30)
    return round(promedio, 1)


def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    nota_final = calcular_promedio(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima()
    estado = evaluar(nota_final)

    print(" ")
    print("---*---*---**-*-** BOLETA --*---*---**-*-**")
    print("Alumno:", nombre_alumno)
    print("Nota de examenes:", nota_examenes)
    print("Nota de tareas:", nota_tareas)
    print("Nota final:", nota_final)
    print("Estado academico:", estado)

    if nota_final < nota_minima:
        print("Examen extraordinario: Si")
    else:
        print("Examen extraordinario: No")


mostrar_encabezado_escuela()
nombre_alumno = input("Ingresa el nombre del alumno: ")
examenes = float(input("Ingresa la calificación de examenes: "))
tareas = float(input("Ingresa la calificación de tareas: "))

generar_boleta(nombre_alumno, examenes, tareas)