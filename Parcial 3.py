class Habito:
    def __init__(self, nombre, frecuencia, duracion):
        self.nombre = nombre
        self.frecuencia = frecuencia
        self.duracion = duracion

def agregar_habito(habitos, nombre, frecuencia, duracion):
    if any(habito.nombre == nombre for habito in habitos):
        print('Error: Hábito duplicado.')
        return
    habito = Habito(nombre, frecuencia, duracion)
    habitos.append(habito)
    ordenar_habitos(habitos)
    print(f"Hábito '{nombre}' agregado.")

def eliminar_habito(habitos, nombre):
    for habito in habitos:
        if habito.nombre == nombre:
            habitos.remove(habito)
            print(f"Hábito '{nombre}' eliminado.")
            return
    print(f"Hábito '{nombre}' no encontrado.")

def mostrar_habitos(habitos):
    if habitos:
        print("Hábitos:")
        for habito in habitos:
            print(f"[Nombre: {habito.nombre}, Frecuencia: {habito.frecuencia} veces/semana, Duración: {habito.duracion} minutos]")
    else:
        print("No hay hábitos registrados.")

def ordenar_habitos(habitos):
    habitos.sort(key=lambda habito: habito.nombre)
    print("Hábitos ordenados por nombre:")
    mostrar_habitos(habitos)

def guardar_habitos_txt(habitos, archivo):
    with open(archivo, 'w') as f:
        for habito in habitos:
            f.write(f"{habito.nombre},{habito.frecuencia},{habito.duracion}\n")
    print(f"Hábitos guardados en {archivo}.")

def cargar_habitos_txt(archivo):
    habitos = []
    try:
        with open(archivo, 'r') as f:
            for line in f:
                nombre, frecuencia, duracion = line.strip().split(',')
                habitos.append(Habito(nombre, int(frecuencia), int(duracion)))
        print(f"Hábitos cargados desde {archivo}.")
    except FileNotFoundError:
        print(f"Archivo {archivo} no encontrado.")
    return habitos

def main():
    habitos = []

    while True:
        print("\nMenú:")
        print("1. Ingresar hábito")
        print("2. Eliminar hábito")
        print("3. Mostrar hábitos")
        print("4. Guardar hábitos en .txt")
        print("5. Cargar hábitos desde .txt")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del hábito: ")
            frecuencia = int(input("Ingrese la frecuencia del hábito (por semana): "))
            duracion = int(input("Ingrese la duración del hábito (en minutos): "))
            agregar_habito(habitos, nombre, frecuencia, duracion)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del hábito a eliminar: ")
            eliminar_habito(habitos, nombre)
        elif opcion == "3":
            mostrar_habitos(habitos)
        elif opcion == "4":
            archivo = input("Ingrese el nombre del archivo .txt para guardar los hábitos: ")
            guardar_habitos_txt(habitos, archivo)
        elif opcion == "5":
            archivo = input("Ingrese el nombre del archivo .txt para cargar los hábitos: ")
            habitos = cargar_habitos_txt(archivo)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
