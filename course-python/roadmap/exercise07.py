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

# functions to show the difference between pass by value and pass by Reference in Python

"""
operations with functions
"""

s1: str = "Hello"
s2: str = "World"

# concaction of strings
print(s1, " ", s2)

print("Pass by Value")


def pass_by_value(value):
    value = 10
    print(value)


value = 20
pass_by_value(value)
print(value)

print("Pass by Reference")


def pass_by_reference(list):
    list[0] = 10
    print(list)


list01: list = [20]
pass_by_reference(list01)
print(list01)
