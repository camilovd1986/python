# Función para agregar notas a la lista de un estudiante
def agregar_notas(estudiante, notas):
    cantidad_notas = int(input(f'¿Cuántas notas deseas agregar para {estudiante}? '))
    for i in range(cantidad_notas):
        nota = float(input(f'Ingrese la nota {i + 1} para {estudiante}: '))
        notas.append(nota)

# Función para calcular el promedio de las notas de un estudiante
def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    else:
        return sum(notas) / len(notas)

# Función para mostrar las notas y el promedio de un estudiante
def mostrar_notas(estudiante, notas):
    print(f'Notas de {estudiante}: {notas}')
    promedio = calcular_promedio(notas)
    print(f'Promedio de {estudiante}: {promedio:.2f}')

# Lista para almacenar las notas de los estudiantes
notas_estudiantes = {}

while True:
    print("\nMenú:")
    print("1. Agregar notas")
    print("2. Mostrar notas y promedio")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre_estudiante = input("Ingrese el nombre del estudiante: ")
        if nombre_estudiante not in notas_estudiantes:
            notas_estudiantes[nombre_estudiante] = []
        agregar_notas(nombre_estudiante, notas_estudiantes[nombre_estudiante])

    elif opcion == "2":
        for estudiante, notas in notas_estudiantes.items():
            mostrar_notas(estudiante, notas)

    elif opcion == "3":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, elija una opción válida.")
