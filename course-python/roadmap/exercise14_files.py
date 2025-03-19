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
#


def add_product(products: dict, file: str):
    name = input("Nombre del producto: ")
    while True:
        try:
            quantity = int(input("Cantidad vendida: "))
            price = float(input("Precio: "))
            total = quantity * price
            break
        except ValueError:
            print("La cantidad y el precio deben ser números.")

    products[name] = {
        "quantity": quantity,
        "unitPrice": price,
        "total": total,
    }
    with open(file, "a") as f:
        f.write(
            f"producto: {name},cantidad_vendida: {quantity},precio_unidad: {
                price
            }, precio_total: {total}\n"
        )

    print("Producto añadido correctamente.")


# this function queries the product by name
def consult_product(products: dict):
    name = input("Nombre del producto: ")
    print("-------------------------")
    if name in products:
        print(f"Producto: {name}")
        print(f"Cantidad vendida: {products[name]['quantity']}")
        print(f"Precio: {products[name]['unitPrice']}")
        print(f"Total: {products[name]['total']}")

    else:
        print("Producto no encontrado.")
    print("-------------------------")


def update_product(products: dict, file: str):
    product_update = input("Nombre del producto a actualizar: ")
    if product_update in products:
        while True:
            try:
                quantity = int(input("Cantidad vendida: "))
                price = float(input("Precio: "))
                total = quantity * price
                break
            except ValueError:
                print("La cantidad y el precio deben ser números.")

        products[product_update] = {
            "quantity": quantity,
            "unitPrice": price,
            "total": total,
        }
        print("Producto actualizado correctamente.")


def delete_product(products: dict):
    product_delete = input("Nombre del producto a eliminar: ")
    if product_delete in products:
        del products[product_delete]
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")


def calculate_total_sale(products: dict):
    if len(products) == 0:
        print("No hay productos.")
        return
    else:
        total = 0
        for product in products.values():
            total += product["total"]
        print(f"Venta total: {total}")


def calculate_sale_by_product(products: dict):
    product = input("Nombre del producto: ")
    if product in products:
        print(f"Venta por producto: {products[product]['total']}")
    else:
        print("Producto no encontrado.")


def main():
    produtcs: dict = {}
    my_file = ""

    while True:
        my_path = input("enter the file name: ")
        if my_path.endswith(".txt"):
            my_file = "./tests/" + my_path
            print(f"the file {my_file} is created successfully.")
            break
        else:
            print("The file name must have the .txt extension")

    while True:
        print("=== Gestión de ventas ===")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Calcular venta total")
        print("6. Calcular venta por producto")
        print("7. Salir")
        print("=========================")

        option = input("Seleccionar una opción: ")

        if option == "1":
            add_product(produtcs, my_file)
        elif option == "2":
            consult_product(produtcs)
        elif option == "3":
            update_product(produtcs, my_file)
        elif option == "4":
            delete_product(produtcs)
        elif option == "5":
            calculate_total_sale(produtcs)
        elif option == "6":
            calculate_sale_by_product(produtcs)
        elif option == "7":
            print("Gracias por usar el programa. hasta la próxima.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
