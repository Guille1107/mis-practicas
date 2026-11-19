from collections import deque
import time
cola_repro=deque()

cola_repro.append("1. Antología")
cola_repro.append("2. Viento")
cola_repro.append("3. Primera cita")

print("Canciones en espera")
for cancion in cola_repro:
    print(" ",cancion)
    print("Iniciando Reproducción")


while cola_repro:
    cancion_actu=cola_repro.popleft()
    print(f"Sonando ahora: {cancion_actu}")
    time.sleep(1)
    print(f"Finalizo: {cancion_actu}")

print(f"Quedan: {len(cola_repro)} canciones en la cola")
print("La reproduccion ha finalizado")