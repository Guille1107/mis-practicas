class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def mostrar_lista(self):
        actual = self.cabeza
        elementos = []
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print("...".join(elementos) + "--None")

lista = ListaEnlazada()
lista.insertar_final("A")
lista.insertar_final("B")
lista.insertar_final("C")
lista.mostrar_lista()
