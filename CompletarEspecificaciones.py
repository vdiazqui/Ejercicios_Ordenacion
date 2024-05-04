def segmento_explorado(t, inicio, fin):
    """
    Verifica si el segmento en la lista 't' ha sido correctamente explorado.

    Parámetros:
        t (list): La lista de elementos.
        inicio (int): El índice inicial del segmento.
        fin (int): El índice final del segmento.

    Retorna:
        bool: True si el segmento se ha explorado correctamente, False de lo contrario.
    """

    # Verificar que los índices sean válidos
    if not (0 <= inicio < len(t)) or not (0 <= fin < len(t)) or inicio > fin:
        return False

    # Encontrar el valor máximo dentro del segmento y su índice
    subsegmento = t[inicio:fin + 1]
    maximo = max(subsegmento)
    indice_maximo = subsegmento.index(maximo)

    # Verificar si el primer elemento es el máximo
    if t[inicio + indice_maximo] != maximo:
        return False

    # Desplazar todos los elementos a la izquierda dentro del rango, excepto el último
    for i in range(inicio + indice_maximo, fin):
        t[i] = t[i + 1]

    # Colocar el valor máximo al final del segmento
    t[fin] = maximo

    return True

# Ejemplo de uso con un segmento no correctamente explorado
valores = [9, 12, 5, 10, 7, 15, 14, 3, 8, 11, 18, 2]

# Segmento que no cumple la condición de exploración
inicio_incorrecto = 2
fin_incorrecto = 6

# Verificar este segmento
exploracion_incorrecta = segmento_explorado(valores, inicio_incorrecto, fin_incorrecto)
print("¿Segmento (incorrecto) explorado correctamente?", exploracion_incorrecta)
print("Lista modificada (incorrecta):", valores)

# Restaurar la lista a su estado original para un ejemplo correcto
valores = [9, 12, 5, 10, 7, 15, 14, 3, 8, 11, 18, 2]

# Segmento que sí cumple la condición
inicio_correcto = 8
fin_correcto = 11

# Verificar este segmento
exploracion_correcta = segmento_explorado(valores, inicio_correcto, fin_correcto)
print("¿Segmento (correcto) explorado correctamente?", exploracion_correcta)
print("Lista modificada (correcta):", valores)
