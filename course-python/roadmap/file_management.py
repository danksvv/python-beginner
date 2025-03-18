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

# method open #1 (this is a type io.TextIOWrapper)
#
# file = open('./tests/data.txt', 'r')
# # print(file)
#
# lines = file.readlines()
# print(lines)
#
# print(type(file))
# file.close()

# method open #2 (this is a type list) this method not require close, "with" it is implicit
#
# with open('./tests/data2.txt', 'r') as my_file:
#     lines = my_file.readlines()
#     new_lines = list(map(lambda line:line.replace('\n',''), lines))
#
#
#     print(lines)
#     print("")
#     print(new_lines)
#     # print(type(lines))
#     print(len(lines))
#
# print(lines)
# print(type(lines))

# method open #3 (this is a type list)
#
# with open('./tests/data2.txt', 'r') as my_file:
#     content = my_file.read()
#     lines = content.split('\n')
#     print(lines)

# count number of characters

# with open('./tests/data2.txt', 'r') as my_file:
#     lines = my_file.readlines()
#     new_lines = list(map(lambda line: line.replace('\n', ''), lines))
#     position = my_file.tell()
#     print(new_lines)
#     print(f"the file is {position} characters long")
#

# printer a portion of the chain
#
# with open('./tests/data2.txt', 'r') as my_file:
#     long = my_file.read(4)
#
#     print(long)

# read in bytes
#
# with open('./tests/data2.txt', 'rb') as my_file:
#     my_bytes = my_file.read()
#     print(my_bytes)

with open("./tests/data3.txt", "w") as my_file:
    my_file.write("this is a line\nthis is a second line\nthis is a third line")
