# /*
# * EJERCICIO:
# * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
# *
# * DIFICULTAD EXTRA (opcional):
# * Crea una agenda de contactos por terminal.
# * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
# * - Cada contacto debe tener un nombre y un número de teléfono.
# * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
# *   los datos necesarios para llevarla a cabo.
# * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
# *   (o el número de dígitos que quieras)
# * - También se debe proponer una operación de finalización del programa.
# */

# Creación de estructuras de datos
# Listas
print("Listas")
my_lista: list = [1, 2, 3, 4, 5]
for i in my_lista:
    print(i)

# tuples
# Las tuplas son inmutables
# No se pueden modificar una vez creadas
# Se pueden acceder a los elementos de la tupla mediante el índice
# Se pueden recorrer con un bucle for
# Se pueden concatenar
print("Tuplas")
my_tupla: tuple = (1, 2, 3, 4, 5, 2)
for i in my_tupla:
    print(i)

print(my_tupla[2])

# Diccionarios
print("Diccionarios")
my_dict: dict = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Conjuntos
# Los conjuntos son colecciones desordenadas de elementos únicos y no indexados
# Se pueden recorrer con un bucle for
print("Conjuntos")
my_set: set = {1, 2, 3, 4, 5, 2}
for i in my_set:
    print(i)

print(f"the size of my_set is {len(my_set)}")

# inserción
# Listas
print("Inserción")
# Se pueden añadir elementos al final de la lista con el método append()
my_lista.append(6)
print(my_lista)
# Se pueden añadir elementos en una posición concreta con el método insert()
my_lista.insert(0, 0)
print(my_lista)
# Se pueden añadir varios elementos a la vez con el método extend()
my_lista.extend([7, 8, 9])
print(my_lista)
# Se pueden añadir elementos al final de la lista con el operador de concatenación
my_lista += [10, 11, 12]
print(my_lista)

# tuples
# insertar un elemento en una tupla no es posible
# Se pueden concatenar
# Se pueden añadir elementos al final de la tupla con el operador de concatenación
my_tupla += (6, 7, 8)
print(my_tupla)

# count y Index
# count() devuelve el número de veces que aparece un elemento en la tupla
# index() devuelve el índice de la primera aparición de un elemento en la tupla
print("count y index")
print(f"the number of times it is repeated 2 in the tuple: {my_tupla.count(2)}")
print(f"the index of the first appearance of 2 in the tuple: {my_tupla.index(2)}")

# Diccionarios
print("Diccionarios")
# Se pueden añadir elementos al diccionario con la clave y el valor
# Se pueden añadir elementos al diccionario con el método update()
my_dict.update({"profesion": "programador"})
print(my_dict)
# Se pueden añadir elementos al diccionario con el método setdefault()
my_dict.setdefault("hobby", "futbol")
print(my_dict)
# copy() devuelve una copia superficial del diccionario
my_copy = my_dict.copy()
print(my_copy)
print(f"my_dict is my_copy: {my_dict is my_copy}")

# borrado
# Listas
print("Borrado")
# Se pueden borrar elementos de la lista con el método remove()
# Si el elemento no existe, se lanza una excepción
my_lista.remove(0)
print(my_lista)
# Se pueden borrar elementos de la lista con el método pop()
my_lista.pop(0)
print(my_lista)
# Se pueden borrar elementos de la lista con el método del y el índice
del my_lista[0]
print(my_lista)

# tuples no se pueden borrar elementos
# Se pueden borrar la tupla entera
del my_tupla

# Diccionarios
# Se pueden borrar elementos del diccionario con el método pop()
my_dict.pop("hobby")
print(my_dict)
# Se pueden borrar elementos del diccionario con el método popitem()
my_dict.popitem()
print(my_dict)
# Se pueden borrar elementos del diccionario con el método del y la clave
del my_dict["ciudad"]
print(my_dict)

# actualización
# Listas
# Se pueden actualizar elementos de la lista con el índice
my_lista[0] = 0
print(my_lista)
# append() añade un elemento al final de la lista
my_lista.append(1)
print(my_lista)
# Se pueden actualizar elementos de la lista con el método extend()
my_lista.extend([2, 3, 4])
print(my_lista)
# insert() añade un elemento en una posición concreta
my_lista.insert(0, -1)
print(my_lista)

# tuples no se pueden actualizar elementos
# Diccionarios
# Se pueden actualizar elementos del diccionario con la clave y el valor
# Se pueden actualizar elementos del diccionario con el método update()
my_dict: dict = {"nombre": "Juan", "edad": "24", "ciudad": "Madrid"}
my_dict.update({"nombre": "Pedro"})
print(my_dict)

# ordenación
# Listas
print("Ordenación")
# Se pueden ordenar los elementos de la lista con el método sort()
my_lista.sort()
print(my_lista)
# Se pueden ordenar los elementos de la lista con el método reverse()
my_lista.reverse()
print(my_lista)
# Se pueden ordenar los elementos de la lista con la función sorted()
print(sorted(my_lista))
# Se pueden ordenar los elementos de la lista con la función reversed()
print(list(reversed(my_lista)))

# tuples no se pueden ordenar elementos
# Se pueden ordenar los elementos de la tupla con la función sorted()
my_tupla: tuple = (1, 2, 3, 4, 5, 2)
print(sorted(my_tupla))
# Se pueden ordenar los elementos de la tupla con la función reversed()

# Diccionarios
# Se pueden ordenar los elementos del diccionario con el método sorted()
print(sorted(my_dict.items()))
# se pueden order por valores con una función lambda
print(sorted(my_dict.items(), key=lambda item: item[1]))
