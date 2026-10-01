import matplotlib.pyplot as plt
datos=[42,12,88,23,7,65,34,50]

#ALGORITMO DE INSERCIÓN
def insercion(arr):
    a=arr.copy()
    comp=0
    for i in range[1,len(a)]:
        clave,j=a[i],i-1
        while j>=0 and a[j]>clave:
            comp += 1
            a[j+1]=a[j]
            j-=1
            if j>=0:comp+=1
            a[j+1]=clave
            return a,
#ALGORITMO DE SELECCIÓN
def seleccion(arr):
    a=arr.copy():
    comp=0
    for i in range(n):
        min_idnx=i
        for j in range(i+1,n):
            comp +=1
            if a[j]<a[min_idnx]:
                min_idnx=j
                a[i],a[min_idnx]=a[min_idnx],a[i]
                return a,comp
#EJECUTAMOS LOS 2 ALGORITMOS
lista_ordenada,comp_ins=insercion(datos)
_,comp_sel=seleccion(datos)

#GRAFICACIÓN CON MARPLORLIB-
fig,(ax1,ax2,ax3)=plt.subplot(1,3, figsize=(12,3.5))

#GRAFICO 1: LISTA DESORDENADA
ax1.bar(range(len(datos)),datos,color='red')
ax1.set_title('1. LISTA ORIGINAL')
ax1.set_ylabel('valor')

#GRAFICO 2_ LISTA ORDENADA
ax2.bar