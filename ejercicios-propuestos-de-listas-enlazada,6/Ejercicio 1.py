class Vehiculo:
    def __init__(self, placa, marca, modelo, año, precio):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
        self.sig = None

class ListaVehiculos:
    def __init__(self): self.cabeza = None

    def agregar(self, placa, marca, modelo, año, precio):
        nuevo = Vehiculo(placa, marca, modelo, año, precio)
        if not self.cabeza: self.cabeza = nuevo
        else:
            act = self.cabeza
            while act.sig: act = act.sig
            act.sig = nuevo

    def buscar(self, placa):
        act = self.cabeza
        while act:
            if act.placa == placa: return act
            act = act.sig
        return None

    def ver_por_año(self, año):
        act, lista = self.cabeza, []
        while act:
            if act.año == año: lista.append(act)
            act = act.sig
        return lista

    def ver_todos(self):
        act, lista = self.cabeza, []
        while act:
            lista.append(act)
            act = act.sig
        return lista

    def eliminar(self, placa):
        act, ant = self.cabeza, None
        while act:
            if act.placa == placa:
                if ant: ant.sig = act.sig
                else: self.cabeza = act.sig
                return True
            ant, act = act, act.sig
        return False

def mostrar(v):
    print(f"{v.placa} - {v.marca} - {v.modelo} - {v.año} - ${v.precio}")

def menu():
    lista = ListaVehiculos()
    while True:
        op = input("\n1.Agregar 2.Buscar 3.Por Año 4.Todos 5.Eliminar 6.Salir: ")
        if op == '1':
            lista.agregar(input("Placa: "), input("Marca: "), input("Modelo: "),
                          input("Año: "), float(input("Precio: ")))
        elif op == '2':
            v = lista.buscar(input("Placa: "))
            mostrar(v) if v else print("No encontrado.")
        elif op == '3':
            for v in lista.ver_por_año(input("Año: ")): mostrar(v)
        elif op == '4':
            for v in lista.ver_todos(): mostrar(v)
        elif op == '5':
            print("Eliminado." if lista.eliminar(input("Placa: ")) else "No encontrado.")
        elif op == '6': break
        else: print("Opción inválida.")

if __name__ == "__main__":
    menu()
