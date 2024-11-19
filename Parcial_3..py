class ListaHabitos:
    def __init__(self):
        self.habitos = []

    def agregar_habito(self, nombre, frecuencia, duracion):
        habito = [nombre, frecuencia, duracion]
        self.habitos.append(habito)
        self.ordenar_habitos()  # Ordenar hábitos automáticamente al agregar uno nuevo
        print(f"Hábito '{nombre}' agregado.")

    def eliminar_habito(self, nombre):
        for habito in self.habitos:
            if habito[0] == nombre:
                self.habitos.remove(habito)
                print(f"Hábito '{nombre}' eliminado.")
                return
        print(f"Hábito '{nombre}' no encontrado.")

    def mostrar_habitos(self):
        if self.habitos:
            print("Hábitos:")
            for habito in self.habitos:
                print(f"[Nombre: {habito[0]}, Frecuencia: {habito[1]} veces/semana, Duración: {habito[2]} minutos]")
        else:
            print("No hay hábitos registrados.")

    def ordenar_habitos(self):
        if self.habitos:
            self.habitos = self.merge_sort(self.habitos)
            print("Hábitos ordenados por nombre:")
            self.mostrar_habitos()
        else:
            print("No hay hábitos registrados para ordenar.")

    def merge_sort(self, lista):
        if len(lista) > 1:
            medio = len(lista) // 2
            izquierda = lista[:medio]
            derecha = lista[medio:]
            self.merge_sort(izquierda)
            self.merge_sort(derecha)
            i = j = k = 0
            while i < len(izquierda) and j < len(derecha):
                if izquierda[i][0] < derecha[j][0]:
                    lista[k] = izquierda[i]
                    i += 1
                else:
                    lista[k] = derecha[j]
                    j += 1
                k += 1
            while i < len(izquierda):
                lista[k] = izquierda[i]
                i += 1
                k += 1
            while j < len(derecha):
                lista[k] = derecha[j]
                j += 1
                k += 1
        return lista

    def guardar_habitos_txt(self, archivo):
        with open(archivo, 'w') as f:
            for habito in self.habitos:
                f.write(f"{habito[0]},{habito[1]},{habito[2]}\n")
        print(f"Hábitos guardados en {archivo}.")

    def cargar_habitos_txt(self, archivo):
        try:
            with open(archivo, 'r') as f:
                self.habitos = [line.strip().split(',') for line in f]
                for habito in self.habitos:
                    habito[1] = int(habito[1])
                    habito[2] = int(habito[2])
            print(f"Hábitos cargados desde {archivo}.")
        except FileNotFoundError:
            print(f"Archivo {archivo} no encontrado.")

def main():
    lista_habitos = ListaHabitos()

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
            lista_habitos.agregar_habito(nombre, frecuencia, duracion)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del hábito a eliminar: ")
            lista_habitos.eliminar_habito(nombre)
        elif opcion == "3":
            lista_habitos.mostrar_habitos()
        elif opcion == "4":
            archivo = input("Ingrese el nombre del archivo .txt para guardar los hábitos: ")
            lista_habitos.guardar_habitos_txt(archivo)
        elif opcion == "5":
            archivo = input("Ingrese el nombre del archivo .txt para cargar los hábitos: ")
            lista_habitos.cargar_habitos_txt(archivo)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
