# /*
# * EJERCICIO:
# * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
# *   su tipo de dato.
# * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
# *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
# * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
# *
# * DIFICULTAD EXTRA (opcional):
# * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
# * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
# *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
# *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
# *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
# *   Comprueba también que se ha conservado el valor original en las primeras.
# */
#

# examples of pass by value and pass by reference in Python

print("Pass by Value")


def pass_by_value_int(value):
    value = 10
    print(value)


value = 20
pass_by_value_int(value)
print(value)


def pass_by_value_str(value):
    value = "World"
    print(value)


value = "Hello"
pass_by_value_str(value)
print(value)


def pass_by_value_float(value):
    value = 10.5
    print(value)


value = 20.5
pass_by_value_float(value)
print(value)


def pass_by_value_bool(value):
    value = False
    print(value)


value = True
pass_by_value_bool(value)
print(value)


def pass_by_value_tuple(value):
    value = (10, 20)
    print(value)


value = (20, 30)
pass_by_value_tuple(value)
print(value)

print("---------------------------------")
print("Pass by Reference")


def pass_by_reference_list(list):
    list[0] = 10
    print(list)


list01: list = [20]
pass_by_reference_list(list01)
print(list01)


def pass_by_reference_dict(dict):
    dict["name"] = "John"
    print(dict)


my_dict: dict = {"country": "Spain"}
pass_by_reference_dict(my_dict)
print(my_dict)

print("---------------------------------")
print("Extra Difficulty")


def swap_values_by_value(value1, value2):
    temp = value1
    value1 = value2
    value2 = temp
    return value1, value2


value1: int = 10
value2: int = 20
print(f"Original values: {value1}, {value2}")
value1, value2 = swap_values_by_value(value1, value2)
print(f"New values: {value1}, {value2}")


def swap_values_by_reference(value1, value2):
    temp = value1
    value1 = value2
    value2 = temp
    return value1, value2


dict1: dict = {"name": "John"}
dict2: dict = {"name": "Jane"}
print(f"Original values: {dict1}, {dict2}")
dict1, dict2 = swap_values_by_reference(dict1, dict2)
print(f"New values: {dict1}, {dict2}")
