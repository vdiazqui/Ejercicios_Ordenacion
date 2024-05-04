# Ejercicios Ordenacion
## Virginia Diaz Quilez
### 2/05/24

# 1.) Ordenacion por Insercion Dicotomica
# 2.) Una ordenación topológica

# 3.) Completar las especificaciones
Este proyecto implementa un algoritmo que verifica si un segmento de una lista ha sido explorado correctamente, según un conjunto de reglas específicas.

## Introducción

El objetivo de este proyecto es identificar si un segmento de una lista cumple con las siguientes reglas:

1. **Identificación del Máximo:** El valor máximo dentro del segmento debe ser el primer elemento.
2. **Desplazamiento:** Todos los elementos en el segmento se desplazan una posición hacia la izquierda, excepto el máximo.
3. **Colocación del Máximo:** El valor máximo se coloca en la última posición del segmento.

## Uso

Para utilizar el código, sigue estos pasos:

1. **Definir los Datos:**
   - Define una lista `valores` que contenga los datos con los que deseas trabajar.
   - Especifica el rango `inicio` y `fin` que define el segmento a explorar.

2. **Ejecutar la Verificación:**
   - Llama a la función `segmento_explorado(valores, inicio, fin)`.
   - Esta función retornará `True` si el segmento fue correctamente explorado según las reglas, o `False` si no cumple con las condiciones.

3. **Resultados:**
   - La lista original se modificará para reflejar el estado del segmento explorado.
