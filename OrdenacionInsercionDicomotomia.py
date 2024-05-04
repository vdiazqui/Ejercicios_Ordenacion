def busqueda_binaria(tabla, clave, inicio, fin):
    """Encuentra la posición de inserción utilizando búsqueda binaria."""
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if tabla[medio] < clave:
            inicio = medio + 1
        else:
            fin = medio - 1
    return inicio

def ordenacion_insercion_dicotomica_en_sitio(tabla):
    """Ordena la tabla usando el método de inserción dicotómica en su lugar."""
    # Empezamos desde el segundo elemento hasta el final
    for i in range(1, len(tabla)):
        clave = tabla[i]  # Elemento actual a insertar
        # Encuentra la posición correcta para el elemento clave usando búsqueda binaria
        posicion = busqueda_binaria(tabla, clave, 0, i - 1)
        # Almacena temporalmente el valor a mover
        valor_temporal = tabla.pop(i)
        # Inserta el valor en la posición correcta
        tabla.insert(posicion, valor_temporal)

# Solicita la entrada del usuario para la tabla
entrada = input("Ingresa los elementos de la tabla separados por espacios: ")
tabla = [int(x) for x in entrada.split()]

print("Tabla original:", tabla)
ordenacion_insercion_dicotomica_en_sitio(tabla)
print("Tabla ordenada:", tabla)


"""
Funcionamiento del Algoritmo: 
  Recorrido Inicial:
El algoritmo comienza recorriendo la lista desde el segundo elemento hasta el final.
Cada elemento se trata como una "clave" que debe colocarse en el lugar correcto dentro de la sección ya ordenada.

  Búsqueda de Posición:
Para cada "clave", se usa una técnica llamada búsqueda binaria para localizar la posición exacta donde debería insertarse dentro de la parte previamente ordenada.
La búsqueda binaria reduce significativamente el número de comparaciones necesarias, ya que descarta la mitad de las posiciones posibles en cada paso.

  Inserción y Desplazamiento:
Una vez identificada la posición correcta, la clave se inserta ahí.
Los elementos existentes entre esa posición y la posición original de la clave son desplazados para hacer espacio.

  Ventajas:
Optimización en Comparaciones: La búsqueda binaria optimiza las comparaciones, ya que reduce el rango de búsqueda en cada iteración, en comparación con la búsqueda lineal del método tradicional de inserción.
Uso de Memoria Eficiente: Todo el proceso se realiza en la misma lista sin requerir almacenamiento adicional, lo que hace que el algoritmo sea eficiente en memoria.

  Desventajas:
Reordenamiento Costoso: Si la lista está muy desordenada o en orden inverso, el costo de mover múltiples elementos para cada nueva inserción puede afectar el rendimiento.
Rendimiento en Grandes Listas: Aunque es una mejora respecto a otros métodos simples, puede no ser ideal para listas con un gran número de elementos debido al desplazamiento necesario.
  Conclusión:
La ordenación por inserción dicotómica utiliza un método eficaz para encontrar el lugar de cada elemento. Aunque sigue presentando algunas limitaciones, es una solución que combina simplicidad y eficiencia, especialmente para listas de tamaño moderado.


"""



