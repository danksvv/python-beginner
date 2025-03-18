# /*
# * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
# *
# * EJERCICIO:
# * Desarrolla un programa capaz de crear un archivo que se llame como
# * tu usuario de GitHub y tenga la extensión .txt.
# * Añade varias líneas en ese fichero:
# * - Tu nombre.
# * - Edad.
# * - Lenguaje de programación favorito.
# * Imprime el contenido.
# * Borra el fichero.
# *
# * DIFICULTAD EXTRA (opcional):
# * Desarrolla un programa de gestión de ventas que almacena sus datos en un
# * archivo .txt.
# * - Cada producto se guarda en una línea del archivo de la siguiente manera:
# *   [nombre_producto], [cantidad_vendida], [precio].
# * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
# *   actualizar, eliminar productos y salir.
# * - También debe poseer opciones para calcular la venta total y por producto.
# * - La opción salir borra el .txt.
# */
import os


def create_file() -> str:
    while True:
        file_name = input("enter the file name: ")
        if file_name.endswith(".txt"):
            return f"./tests/{file_name}"
        print("The file name must have the .txt extension")


def enter_data() -> dict:
    data = {}
    data["name"] = input("Enter your name: ")
    data["age"] = input("Enter your age: ")
    data["favorite_programming_language"] = input(
        "Enter your favorite programming language: "
    )
    return data


def write_file(file_name: str) -> None:
    data = enter_data()
    with open(file_name, "w") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")


def read_file(file_name: str) -> None:
    with open(file_name, "r") as file:
        print(file.read())


def delete_file(file_name: str) -> None:
    os.remove(file_name)


def main():
    file_name = ""
    while True:
        print("=== File Management ===")
        print("1. Create file")
        print("2. Write file")
        print("3. Read file")
        print("4. Delete file")
        print("5. Exit")
        option = input("Enter an option: ")
        if option == "1":
            file_name = create_file()
        elif option == "2":
            write_file(file_name)
        elif option == "3":
            read_file(file_name)
        elif option == "4":
            delete_file(file_name)
        elif option == "5":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
