# Lista de estudiantes (nombre, calificacion)
estudiantes = [
    ("Ana", 85),
    ("Luis", 90),
    ("Carlos", 78),
    ("Marta", 92),
    ("Jorge", 88)
]

# 1. Ordenar estudiantes por calificacion de mayor a menor usando Quicksort
def quicksort_calificacion(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    mayores = [x for x in lista[1:] if x[1] > pivote[1]]
    iguales = [x for x in lista if x[1] == pivote[1]]
    menores = [x for x in lista[1:] if x[1] < pivote[1]]
    return quicksort_calificacion(mayores) + iguales + quicksort_calificacion(menores)

estudiantes_ordenados = quicksort_calificacion(estudiantes)

print("Estudiantes ordenados por calificacion (mayor a menor):")
for nombre, calificacion in estudiantes_ordenados:
    print(f"{nombre}: {calificacion}")

# 2. Quicksort para ordenar alfabéticamente por nombre
def quicksort_nombres(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x[0] < pivote[0]]
    iguales = [x for x in lista if x[0] == pivote[0]]
    mayores = [x for x in lista[1:] if x[0] > pivote[0]]
    return quicksort_nombres(menores) + iguales + quicksort_nombres(mayores)

estudiantes_por_nombre = quicksort_nombres(estudiantes)

# Búsqueda binaria por nombre (requiere lista ordenada alfabéticamente)
def busqueda_binaria(lista_ordenada, nombre_buscar):
    izquierda = 0
    derecha = len(lista_ordenada) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        nombre_actual = lista_ordenada[medio][0]
        if nombre_actual == nombre_buscar:
            return f"{nombre_actual} tiene una calificacion de {lista_ordenada[medio][1]}."
        elif nombre_actual < nombre_buscar:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return f"{nombre_buscar} no esta en la lista."

# Prueba de búsqueda
nombre_a_buscar = "Carlos"
resultado_busqueda = busqueda_binaria(estudiantes_por_nombre, nombre_a_buscar)
print("\nResultado de la busqueda:")
print(resultado_busqueda)