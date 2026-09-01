# LISTAS BIDIMENSIONALES
#Ejercicio 1: Crear una matriz de numeros 
# =============================================================
def crear_matriz(filas, columnas):
    matriz = []
    contador = 1
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(contador)
            contador += 1
        matriz.append(fila)
        
    return matriz

# Example usage:
resultado = crear_matriz(3, 4)
for fila in resultado:
    print(fila)

#Ejercicio 2: Suma de Todos los Elementos
# =============================================================
lista_bidimensional = [[1,2,3],[4,5,6],[7,8,9]]
suma_bidimensional = 0
for fila in lista_bidimensional:
    for numero in fila:
        suma_bidimensional += numero
print(f"El total de la lista es de {suma_bidimensional}")

#Ejercicio 3: Suma de Cada Fila 
# ============================================================= 
for fila in lista_bidimensional:
    suma_bidimensional = 0
    for numero in fila:
        suma_bidimensional += numero
    print(f"El valor de la fila {fila} es {suma_bidimensional}")

#Ejercicio 4: Matriz Transpuesta 
# ============================================================= 
print("Matriz original")
for fila in lista_bidimensional:
    print(fila)

print("Matriz transpuesta")
matriz = []
for columna in range(len(lista_bidimensional[0])):
    nueva_fila = []
    for fila in range(len(lista_bidimensional)):
        nueva_fila.append(lista_bidimensional[fila][columna])
    matriz.append(nueva_fila)
    print(nueva_fila)

# Ejercicio 5: Encontrar el Elemento Mayor
# =============================================================
lista_mayor = [numero for fila in lista_bidimensional for numero in fila]
mayor = max(lista_mayor)
print(f"El valor más grande de la lista es {mayor}")

#Ejercicio 6: Multiplicar una Matriz por un Escalar 
# ============================================================= 
escalado = int(input("Ingrese un valor para escalar la lista: "))
print("Lista original")
for fila in lista_bidimensional:
    print(fila)

print()
print("lista escalada")
lista_multiplicada = []
for fila in lista_bidimensional:
    nueva_fila = []
    for numero in fila:
        nueva_fila.append(numero * escalado)
    lista_multiplicada.append(nueva_fila)
    print(nueva_fila)
#Ejercicio 7: Diagonal de una Matriz Cuadrada 
# =============================================================
matriz_principal = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
diagonal = []
for i in range(len(matriz_principal)):
    diagonal.append(matriz_principal[i][i])

print(f"Diagonal principal: {diagonal}")

#Ejercicio 8: Matriz Identidad 
# =============================================================
n = 3
matriz_identidad = []
print("matriz identidad")
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz_identidad.append(fila)
    print(fila)

#Ejercicio 9: Matriz Identidad Inversa 
# =============================================================
n = 3
matriz_identidad_inversa = []
print("matriz identidad")
for horizontal in range(n):
    fila = []
    for columna in range(n):
        if columna + horizontal == n - 1:
            fila.append(1)
        else:
            fila.append(0)
    matriz_identidad_inversa.append(fila)
    print(fila)

#Ejercicio 10: Verificar Matriz Simétrica 
# =============================================================
matriz_simetrica = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
]
matriz_transpuesta = []
for horizontal in range(len(matriz_simetrica[0])):
    fila = []
    for columna in range(len(matriz_simetrica)):
        fila.append(matriz_simetrica[columna][horizontal])
    matriz_transpuesta.append(fila)

if matriz_simetrica == matriz_transpuesta:
    print("Es una matriz simétrica")
else:
    print("No es una matriz simétrica")

#Ejercicio 11:Rotar una matriz a 90 grados
# =============================================================
def ejercicio_11():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    n = len(matriz)
    nueva = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            nueva[j][n - 1 - i] = matriz[i][j]
    
    for fila in nueva:
        print(fila)

ejercicio_11()

#Ejercicio 12: Analizador y Filtrado de calificaciones
# =============================================================
notas = "45, 88, -5, 92, 30, 110, 75, 60, 15"
aprobados = []
reprobados = []
notas_validas = []
lista_notas = notas.split(", ")
for nota in lista_notas:
    nota_num = int(nota) 
    if nota_num < 0 or nota_num > 100:
        continue
    notas_validas.append(nota_num)
    if nota_num >= 60:
        aprobados.append(nota_num)
    else:
        reprobados.append(nota_num)

promedio = sum(notas_validas) / len(notas_validas)
ultimos_aprobados = aprobados[-2:]
print("Últimos 2 aprobados registrados:", ultimos_aprobados)

print("El promedio es", promedio)
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)

#Ejercicio 13: Gestor Interactivo de Proyectos con while y Operador in 
# =============================================================
tareas = []
sistema = 0

while sistema != 4:
    sistema = int(input("""---GESTOR INTERACTIVO---
1.Agregar tarea
2.Eliminar tarea
3.Ver resumen
4.Salir
"""))
    if sistema == 1:
        tarea = input("Ingrese el nombre de su tarea: ")
        if tarea in tareas:
            print("Esta tarea ya esta registrada.")
        else:
            tareas.append(tarea)
    if sistema == 2:
        nombre_tarea = input("Ingrese la tarea a eliminar: ")
        if nombre_tarea in tareas:
            tareas.remove(nombre_tarea)
        else:
            print("Esa tarea no esta registrada.")
    if sistema == 3:
        primeras_3_tareas = ", ".join(tareas[:3])
        print(f"""El total de tareas que se han registrado son: {len(tareas)}
Las Primeras 3 tareas son: {primeras_3_tareas}""")
    if sistema == 4:
        break
