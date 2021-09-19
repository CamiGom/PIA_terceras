listaLibros = []

class Libros(object):
    def __init__(self, _titulolibro, _autor, _editorial, _libroprestado, _librodevuelto):
        self.titulolibro = _titulolibro
        self.autor = _autor
        self.editorial = _editorial
        self.libroprestado = _libroprestado
        self.librodevuelto = _librodevuelto

    def entregarDatos(self):
        print("Título libro: {} - Autor: {} - Editorial: {} - Libro Prestado {} - Libro Devuelto {} ".format(self.titulolibro, self.autor, self.editorial, self.libroprestado, self.librodevuelto))
  


def registrarLibro():
    print("Registro de Libros\n")
    titulolibro = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    editorial = input("Ingrese la editorial: ")
    libroprestado = input("Ingrese si el libro ha sido prestado [S/N]: ")
    librodevuelto = input("Ingrese si el libro ha sido devuelto [S/N]: ")
    objLibros = Libros(titulolibro, autor, editorial, libroprestado, librodevuelto)
    listaLibros.append(objLibros)

def listadoLibros():
    print("Listado de Libros\n")
    for objLibros in listaLibros:
        objLibros.entregarDatos()

def buscarLibro():
    print("Buscar Libro\n")
    titulolibro = input("Ingrese el título del libro a buscar: ")
    for objLibros in listaLibros:
        if titulolibro == objLibros.titulolibro:
            objLibros.entregarDatos()

            
def salir():
    print("***** ¡ Gracias por utilizar el programa ! :) ***** ")
    exit()

def main():
    while True:
        print("\n")
        print("|****************************|")
        print("|**|      Bienvenidos     |**|")
        print("|**|         Menu         |**|")
        print("|****************************|")
        print("")
        print("Seleccione una de las siguientes opciones:");
        print("1.- Registrar Libro")
        print("2.- Mostrar Listado de Libros")
        print("3.- Buscar Libro")
        print("4.- Salir\n")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            registrarLibro()
        elif opcion == 2:
            listadoLibros()
        elif opcion == 3:
            buscarLibro()
        elif opcion == 4:
            salir()

if __name__ == '__main__':
    main();