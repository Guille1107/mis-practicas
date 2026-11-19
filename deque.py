from collections import deque
cola=deque()

cola.append("cliente 1")
cola.append("cliente 2")
cola.append("cliente 3")

atendido=cola.popleft()

print("Atendido: ",atendido)
print("Cola restante: ",cola)