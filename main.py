import json
import os
from pathlib import Path
#Obtener la ruta del directorio donde se encuentra la biblioteca
SCRIPT_DIR = Path(__file__).resolve().parent
#Definir la ruta completa del archivo de la biblioteca
DATA_FILE = SCRIPT_DIR / "biblioteca.json"

def load_libros():

    try:
        with open(DATA_FILE,'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError: # Si el archivo no existe que retorne una lista vacio o data inicial.
        return [
    {
        "Titulo": "Cien años de soledad",
        "Autor": "Gabriel García Márquez",
        "Año": 1967,
        "ISBN": "978-3-1-148410-0"
    },
    {
        "Titulo": "Don Quijote de la Mancha",
        "Autor": "Miguel de Cervantes",
        "Año": 1605,
        "ISBN": "978-1-23-456789-7"
    },
    {
        "Titulo": "La casa de los Espíritus",
        "Autor": "Isabel Allende",
        "Año": 1982,
        "ISBN": "978-0-12-345678-9"
    }

]
  
    except json.JSONDecodeError: # If file is not json
        print("No se pudo decodificar la informacion del archivo.")
        return [
    {
        "Titulo": "Cien años de soledad",
        "Autor": "Gabriel García Márquez",
        "Año": 1967,
        "ISBN": "978-3-1-148410-0"
    },
    {
        "Titulo": "Don Quijote de la Mancha",
        "Autor": "Miguel de Cervantes",
        "Año": 1605,
        "ISBN": "978-1-23-456789-7"
    },
    {
        "Titulo": "La casa de los Espíritus",
        "Autor": "Isabel Allende",
        "Año": 1982,
        "ISBN": "978-0-12-345678-9"
    }
]

def save_libros(libros_data):
    with open(DATA_FILE,'w', encoding='utf-8') as f:
            json.dump(libros_data, f, indent=4, ensure_ascii=False)
        
def display_libros(libros_data):
     if not libros_data:
          print("No hay libros en la biblioteca.")
          print("")
          return 
     for i, libro in enumerate(libros_data):
          print(f"{i+1}. Titulo: {libro["Titulo"]}, Autor: {libro["Autor"]}, Año: {libro["Año"]}, ISBN: {libro["ISBN"]}")
          print("-"*120)
          print("")

def add_libro(libros_data):
     
     print("")
     titulo = input("Ingrese el titulo del libro: ")
     print("")
     autor = input("Ingrese el nombre del autor del libro: ")
     print("")
     while True:
            try:
               anio = int(input("Ingrese el año de publicacion del libro: "))
               print("")
               break
            except ValueError: # Si el try da error de valor (tipo de dato.)
               print("Entrada invalida. Por favor ingrese un numero para espcificar el año.")
               print("")

     isbn = input("Ingrese el ISBN del libro: ")
     print("")

     nuevo_libro = {
          "Titulo":titulo,
          "Autor":autor,
          "Año":anio,
          "ISBN":isbn

     }

     print("")

     libros_data.append(nuevo_libro)
     save_libros(libros_data)
     print(f"{titulo} ha sido añadido a la biblioteca.")
     print("")

def modify_libros(libros_data):
     display_libros(libros_data)

     indice_book = int(input("Ingrese el numero del libro que desea modificar: ")) - 1
     print("")
    
     titulo = input("Ingrese el titulo del libro: ")
     print("")
     autor = input("Ingrese el nombre del autor del libro: ")
     print("")
     while True:
            try:
               anio = int(input("Ingrese el año de publicacion del libro: "))
               print("")
               break
            except ValueError: # Si el try da error de valor (tipo de dato.)
               print("Entrada invalida. Por favor ingrese un numero para espcificar el año.")
               print("")

     isbn = input("Ingrese el ISBN del libro: ")
     print("")

     modify_book= {
          "Titulo":titulo,
          "Autor":autor,
          "Año":anio,
          "ISBN":isbn
     }
    
     libros_data[indice_book] = modify_book
     print(libros_data[indice_book])
     save_libros(libros_data)
     return 
    
    

def delete_libros(libros_data):
    display_libros(libros_data)
    if not libros_data:
        return
    while True:
          try:
               index = int(input("Ingrese el numero del libro que dese eliminar: "))
               print("")
               if 0 <= len(libros_data):
                    break
               else: 
                    print("El numero de libro es invalido. Intentelo de nuevo.")
                    print("")
          except ValueError:
               print("Debe de ingresar el numero de la lista de libros.")
               print("")
    
    libro_eliminado = libros_data.pop(index)
    save_libros(libros_data)
    print(f"{libro_eliminado} ha sido borrado de la biblioteca.")

def main():
     libros = load_libros()

     while True:
        print("\n---- Menu de la Bibliote ----\n")
        print("1. Ver todos los libros.")
        print("2. Agregar un libro.")
        print("3. Modificar un libro.")
        print("4. Eliminar un libro.")
        print("5. Salir")

        print("")
        choice = input("Por favor seleccione una opcion (1-5): ")
        print("")

        if choice == "1":
            display_libros(libros)
            print("")
        elif choice == "2":
             add_libro(libros)
             print("")
        elif choice == "3":
            modify_libros(libros)
            print("")
        elif choice == "4":
             delete_libros(libros)
             print("")
        elif choice == "5":
             print("Saliendo del programa...")
             print("")
             break
        else:
             print("Ingrese una opcion valida. (1-5)")
             print("")
        
if __name__ == "__main__":
     main()