class Estudiante:
    def __init__(self, cedula, nombre, apellido, correo, nota):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.nota = nota
        self.sig = None

class ListaEstudiantes:
    def __init__(self):
        self.inicio = None

    def agregar(self, ced, nom, ape, cor, nota):
        nuevo = Estudiante(ced, nom, ape, cor, nota)
        if nota >= 6:
            nuevo.sig = self.inicio
            self.inicio = nuevo
        else:
            if not self.inicio:
                self.inicio = nuevo
            else:
                actual = self.inicio
                while actual.sig:
                    actual = actual.sig
                actual.sig = nuevo

    def buscar(self, cedula):
        actual = self.inicio
        while actual:
            if actual.cedula == cedula:
                return actual
            actual = actual.sig
        return None

    def eliminar(self, cedula):
        actual, anterior = self.inicio, None
        while actual:
            if actual.cedula == cedula:
                if anterior:
                    anterior.sig = actual.sig
                else:
                    self.inicio = actual.sig
                return True
            anterior, actual = actual, actual.sig
        return False

    def contar_aprobados(self):
        actual, total = self.inicio, 0
        while actual:
            if actual.nota >= 6:
                total += 1
            actual = actual.sig
        return total

    def contar_reprobados(self):
        actual, total = self.inicio, 0
        while actual:
            if actual.nota < 6:
                total += 1
            actual = actual.sig
        return total

def mostrar(e):
    print(f"{e.cedula} - {e.nombre} {e.apellido} - {e.correo} - Nota: {e.nota}")

def menu():
    lista = ListaEstudiantes()
    while True:
        op = input("\n1.Agregar 2.Buscar 3.Eliminar 4.Total Aprobados 5.Total Reprobados 6.Salir: ")
        if op == '1':
            lista.agregar(
                input("Cédula: "),
                input("Nombre: "),
                input("Apellido: "),
                input("Correo: "),
                float(input("Nota (1-10): "))
            )
        elif op == '2':
            e = lista.buscar(input("Cédula: "))
            mostrar(e) if e else print("No encontrado.")
        elif op == '3':
            print("Eliminado." if lista.eliminar(input("Cédula: ")) else "No encontrado.")
        elif op == '4':
            print("Total aprobados:", lista.contar_aprobados())
        elif op == '5':
            print("Total reprobados:", lista.contar_reprobados())
        elif op == '6':
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
