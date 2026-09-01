#Ejercicio 1: Suma de Elementos
# =============================================================
cantidad = int(input("Ingrese la cantidad de elementos quiere añadir en la lista: "))
elemento = 0
listaNumeros = []

for i in range(cantidad):
    elemento = int(input("Ingrese el elemento que desea añadir: "))
    listaNumeros.append(elemento)
    print(listaNumeros)

suma = sum(listaNumeros)
print(suma)
#Ejercicio 2: Encontrar el Mayor y el Menor
# =============================================================
cantidad = int(input("Ingrese la cantidad de elementos quiere añadir en la lista: "))
elemento = 0
listaNumeros = []

for i in range(cantidad):
    elemento = int(input("Ingrese el elemento que desea añadir: "))
    listaNumeros.append(elemento)
    print(listaNumeros)

print(f"Valor maximo: {max(listaNumeros)}")
print(f"Valor minimo: {min(listaNumeros)}")

#Ejercicio 3: Invertir una Lista
# =============================================================
cantidad = int(input("Ingrese la cantidad de elementos quiere añadir en la lista: "))
elemento = 0
listaNumeros = []

for i in range(cantidad):
    elemento = int(input("Ingrese el elemento que desea añadir: "))
    listaNumeros.append(elemento)
    print(listaNumeros)

listaNumeros.reverse()
print(f"{listaNumeros}")


#Ejercicio 4: Contar Elementos Pares e Impares
# =============================================================
contadorPares = 0
contadorImpares = 0

cantidad = int(input("Ingrese la cantidad de elementos quiere añadir en la lista: "))
elemento = 0
listaNumeros = []

for i in range(cantidad):
    elemento = int(input("Ingrese el elemento que desea añadir: "))
    if elemento % 2 == 0:
        contadorPares += 1
    else:
        contadorImpares += 1

    listaNumeros.append(elemento)
    print(listaNumeros)

print(f"Hay un total de {contadorPares} números pares")
print(f"Hay un total de {contadorImpares} números impares")


#Ejercicio 5: Multiplicar elemento por un valor
# =============================================================
lista=[]
num=int(input("Ingrese la lista de numeros y 0 para salir"))
while num!=0:
    lista.append(num)
    num= int(input("Ingrese la lista de numeros"))
valor=int(input("INGRESE UN VALOR POR EL CUAL QUIERE MULTIPLICAR CADA ELEMENTO DE LA LISTA"))
for i in range(len(lista)):
    lista[i]=lista[i]*valor
print(lista)

#Ejercicio 6: Eliminar duplicados
# =============================================================
lista=[]
num=int(input("Ingrese la lista de numeros y 0 para salir"))
while num!=0:
    lista.append(num)
    num= int(input("Ingrese la lista de numeros"))
lista=list(set(lista))
print(lista)

#Ejercicio 7: Promedio de una lista
# =============================================================
lista=[]
num=int(input("Ingrese la lista de numeros y 0 para salir"))
while num!=0:
    lista.append(num)
    num= int(input("Ingrese la lista de numeros"))
contador=0
suma=sum(lista)   
for i in lista:
    contador+=1 
promedio=suma/contador
print("El promedio es", promedio)

#Ejercicio 8: Encontrar Elementos Repetidos
# =============================================================
listaNumeros = [1, 2, 3, 4, 2, 7, 3, 8, 1, 9, 4, 4]
conteo = {}
for elemento in listaNumeros:
    if elemento in conteo:
        conteo[elemento] += 1
    else:
        conteo[elemento] = 1
print("Elementos repetidos (diccionario):")
for elemento, cantidad in conteo.items():
    if cantidad > 1:
        print(f"{elemento} aparece {cantidad} veces")
vistos = set()
repetidos = set()
for elemento in listaNumeros:
    if elemento in vistos:
        repetidos.add(elemento)
    else:
        vistos.add(elemento)
print("\nElementos repetidos (set):")
print(repetidos)

# Ejercicio 9: Lista de Numeros Primos
# =============================================================
def es_primo(numero):
    """Devuelve True si 'numero' es primo, False en caso contrario."""
    if numero < 2:
        return False
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False
    return True
 
 
def ejercicio_9():
    datos = input("Ingrese una lista de numeros separados por comas: ")
    lista = [int(x.strip()) for x in datos.split(",")]
 
    primos = [n for n in lista if es_primo(n)]
 
    print(f"Lista original: {lista}")
    print( "Numeros primos: {primos}")

# Ejercicio 10: Eliminar un Elemento por su indice
# =============================================================
def ejercicio_10():
    datos = input("Ingrese una lista de numeros separados por comas: ")
    lista = [int(x.strip()) for x in datos.split(",")]
 
    indice = int(input(f"Ingrese el indice a eliminar (0 a {len(lista) - 1}): "))
 
    if 0 <= indice < len(lista):
        del lista[indice]
        print(f"Lista despues de eliminar el indice {indice}: {lista}")
    else:
        print("indice fuera de rango.")
 
 
# =============================================================
# Ejercicio 11: Contar Ocurrencias de un Elemento
# =============================================================
def ejercicio_11():
    datos = input("Ingrese una lista de numeros separados por comas: ")
    lista = [int(x.strip()) for x in datos.split(",")]
 
    numero = int(input("Ingrese el numero a buscar: "))
    ocurrencias = lista.count(numero)
 
    print(f"El numero {numero} aparece {ocurrencias} veces en la lista.")
 
 
# =============================================================
# Ejercicio 12: Sumar Listas Elemento por Elemento
# =============================================================
def ejercicio_12():
    datos1 = input("Ingrese la primera lista de numeros separados por comas: ")
    lista1 = [int(x.strip()) for x in datos1.split(",")]
 
    datos2 = input("Ingrese la segunda lista de numeros separados por comas: ")
    lista2 = [int(x.strip()) for x in datos2.split(",")]
 
    if len(lista1) != len(lista2):
        print("Error: las listas deben tener la misma longitud.")
        return
 
    suma = [a + b for a, b in zip(lista1, lista2)]
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Suma elemento por elemento: {suma}")
 
 
# =============================================================
# Ejercicio 13: NumPy para trabajar con matrices y arrays
# =============================================================
def ejercicio_13():
    """
    NumPy es una libreria de Python especializada en calculo numerico y
    manejo de arrays/matrices de forma mucho mas eficiente que las listas
    nativas de Python. Sus arrays (ndarray) ocupan menos memoria y permiten
    realizar operaciones matematicas vectorizadas (sin necesidad de bucles
    for explicitos), lo cual es mucho mas rapido para grandes volumenes
    de datos.
 
    Instalacion: pip install numpy
    """
    import numpy as np
 
    # Crear un array a partir de una lista
    array = np.array([1, 2, 3, 4, 5])
    print("Array 1D:", array)
 
    # Crear una matriz (array 2D)
    matriz = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print("Matriz 2D:\n", matriz)
 
    # Operaciones basicas vectorizadas (sin bucles)
    print("Array + 10:", array + 10)
    print("Array * 2:", array * 2)
 
    # Suma, maximo, minimo y promedio
    print("Suma de la matriz:", matriz.sum())
    print("Maximo de la matriz:", matriz.max())
    print("Minimo de la matriz:", matriz.min())
    print("Promedio de la matriz:", matriz.mean())
 
    # Transponer una matriz (filas <-> columnas)
    print("Matriz transpuesta:\n", matriz.T)
 
    # Producto matricial
    identidad = np.eye(3)  # matriz identidad 3x3
    print("Producto matriz x identidad:\n", matriz.dot(identidad))
 
    # Forma (dimensiones) del array
    print("Forma de la matriz:", matriz.shape)
 
 
# =============================================================
# Menu principal para probar cada ejercicio
# =============================================================
if __name__ == "__main__":
    ejercicios = {
        "9": ejercicio_9,
        "10": ejercicio_10,
        "11": ejercicio_11,
        "12": ejercicio_12,
        "13": ejercicio_13,
    }
 
    print("Ejercicios disponibles: 9, 10, 11, 12, 13")
    opcion = input("Que ejercicio queres ejecutar?: ").strip()
 
    if opcion in ejercicios:
        print(f"\n--- Ejecutando Ejercicio {opcion} ---")
        ejercicios[opcion]()
    else:
        print("Opcion no valida.")