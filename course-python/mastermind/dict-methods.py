# Características principales de los diccionarios

# Pares clave-valor: Cada elemento en un diccionario tiene una clave y un valor asociado.
# Mutables: Puedes modificar, agregar o eliminar elementos después de crear el diccionario.
# Desordenados (antes de Python 3.7): No garantizan un orden específico.
# Claves únicas: No puede haber dos claves iguales en un diccionario.
# Eficientes: Las operaciones de búsqueda, inserción y eliminación son muy rápidas.
#
#

my_dict = {"name": "John", "age": 36, "country": "Norway"}
print(my_dict)

# empty dictionary
my_dict = {}

# other way to create a dictionary
other_dict = dict(name="John", age=36, country="Norway")
print(other_dict)

# methods to access the values of a dictionary
my_dict_keys = my_dict.keys()
print(my_dict_keys)

# methods to access the values of a dictionary
print(my_dict.values())

# items method returns a view object that displays a list of a dictionary's key-value tuple pairs
print(my_dict.items())

# update() method adds element(s) to the dictionary if the key is not in the dictionary
my_dict.update({"name": "Jane", "age": 25})
print(my_dict)

# pop() method removes the item with the specified key name
my_dict.pop("name")
print(my_dict)

# popitem() method removes the last inserted item
my_dict.popitem()
print(my_dict)

# clear() method removes all the elements from a dictionary
my_dict.clear()
print(my_dict)

# operations with dictionaries
# add or modify elements in a dictionary
my_dict = {"name": "John", "age": 36, "country": "Norway"}
my_dict["name"] = "Jane"
my_dict["city"] = "New York"
print(my_dict)

# delete or remove elements in a dictionary
del my_dict["name"]
print(my_dict)

# check if a key exists in a dictionary
if "name" in my_dict:
    print("the key 'name' exists in the dictionary")

my_dict.clear()
# loop through a dictionary

my_dict = {"name": "John", "age": 36, "country": "Norway"}
for key in my_dict:
    print(key)
