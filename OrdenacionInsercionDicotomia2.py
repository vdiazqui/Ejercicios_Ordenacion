def insercion_binaria(lista):
    """Ordena la lista utilizando una inserción binaria con lista auxiliar."""
    # Inicializa una lista auxiliar que contendrá los elementos ordenados
    auxiliar = [None] * len(lista)
    num_elementos_ordenados = 0

    # Recorre cada valor de la lista original
    for valor in lista:
        # Variables para definir los límites de la búsqueda binaria
        inicio, fin = 0, num_elementos_ordenados - 1

        # Realiza una búsqueda binaria para encontrar la posición de inserción
        while inicio <= fin:
            medio = (inicio + fin) // 2  # Calcula el índice medio
            if valor < auxiliar[medio]:  # Si el valor es menor, busca a la izquierda
                fin = medio - 1
            else:  # De lo contrario, busca a la derecha
                inicio = medio + 1

        # Desplaza los elementos hacia la derecha para hacer espacio
        for j in range(num_elementos_ordenados, inicio, -1):
            auxiliar[j] = auxiliar[j - 1]

        # Coloca el valor en el índice encontrado por la búsqueda binaria
        auxiliar[inicio] = valor
        num_elementos_ordenados += 1  # Incrementa el contador de elementos ordenados

    return auxiliar  # Devuelve la lista auxiliar ordenada

# Solicita al usuario ingresar datos para la lista
entrada_usuario = input("Ingresa una lista de números separados por espacios: ")
numeros = [int(x) for x in entrada_usuario.split()]

# Llama a la función de ordenación para obtener el resultado ordenado
lista_ordenada = insercion_binaria(numeros)

# Imprime los resultados originales y ordenados
print("Lista original:", numeros)
print("Lista ordenada:", lista_ordenada)
