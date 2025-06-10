# Funcion de ordenamiento burbuja (Bubble Sort)
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Funcion de ordenamiento por insercion (Insertion Sort)
def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        valor = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > valor:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor
    return lista

# Busqueda lineal: recorre todos los elementos uno a uno
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Devuelve la posicion
    return -1  # No encontrado

# Busqueda binaria: requiere que la lista este ordenada
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1  # No encontrado

# Programa principal
numeros = [23, 5, 1, 56, 12, 8, 45]
objetivo = 12

print("Lista original:", numeros)

# Ordenar usando burbuja
orden_burbuja = ordenamiento_burbuja(numeros.copy())
print("\nOrdenada con burbuja:", orden_burbuja)

# Ordenar usando insercion
orden_insercion = ordenamiento_insercion(numeros.copy())
print("Ordenada con insercion:", orden_insercion)

# Busqueda lineal (no necesita lista ordenada)
pos_lineal = busqueda_lineal(numeros, objetivo)
print(f"\nBusqueda lineal: El numero {objetivo} se encuentra en la posicion {pos_lineal}" if pos_lineal != -1 else "No encontrado con busqueda lineal.")

# Busqueda binaria (requiere lista ordenada)
pos_binaria = busqueda_binaria(orden_burbuja, objetivo)
print(f"Busqueda binaria: El numero {objetivo} se encuentra en la posicion {pos_binaria}" if pos_binaria != -1 else "No encontrado con busqueda binaria.")
