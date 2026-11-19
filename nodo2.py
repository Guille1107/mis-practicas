class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None

#Creación de nodo individual

nodo_singular=Nodo("Primer dato")
print(nodo_singular.dato)
print(nodo_singular.siguiente)