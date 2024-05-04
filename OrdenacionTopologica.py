from collections import defaultdict, deque

def ordenacion_topologica_kahn(n, restricciones):
    # Crear el grafo con listas de adyacencia y grados de entrada
    grafo = defaultdict(list)
    grados_entrada = [0] * n

    # Llenar el grafo y calcular los grados de entrada
    for predecesor, sucesor in restricciones:
        grafo[predecesor - 1].append(sucesor - 1)
        grados_entrada[sucesor - 1] += 1

    # Crear una cola con nodos de grado de entrada cero
    cola = deque([i for i in range(n) if grados_entrada[i] == 0])
    orden = []

    # Procesar los nodos de la cola
    while cola:
        tarea = cola.popleft()
        orden.append(tarea + 1)

        # Reducir el grado de entrada de las tareas sucesoras
        for sucesor in grafo[tarea]:
            grados_entrada[sucesor] -= 1
            if grados_entrada[sucesor] == 0:
                cola.append(sucesor)

    # Verificar si la longitud del orden es igual a n
    if len(orden) != n:
        return "No se puede realizar la ordenación debido a un ciclo."
    return orden

# Solicitar al usuario el número total de tareas
try:
    n = int(input("Ingrese el número total de tareas: "))
    if n <= 0:
        raise ValueError("El número de tareas debe ser positivo.")
except ValueError as e:
    print(f"Error: {e}")
    exit()

# Solicitar restricciones de precedencia
restricciones = []
print("Ingrese las restricciones de precedencia en formato 'i j'.")
print("Ingrese '0 0' para finalizar.")

while True:
    entrada = input("Restricción: ").strip()
    if entrada == '0 0':
        break
    try:
        i, j = map(int, entrada.split())
        if 1 <= i <= n and 1 <= j <= n:
            restricciones.append((i, j))
        else:
            print(f"Error: las tareas deben estar en el rango de 1 a {n}.")
    except ValueError:
        print("Error: por favor, ingrese dos números enteros válidos.")

# Calcular el orden de las tareas con las restricciones dadas
resultado = ordenacion_topologica_kahn(n, restricciones)
print("Orden de las tareas:", resultado)
