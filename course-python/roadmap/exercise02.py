# /*
# * EJERCICIO:
# * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
# *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
# *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
# * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
# *   que representen todos los tipos de estructuras de control que existan
# *   en tu lenguaje:
# *   Condicionales, iterativas, excepciones...
# * - Debes hacer print por consola del resultado de todos los ejemplos.
# *
# * DIFICULTAD EXTRA (opcional):
# * Crea un programa que imprima por consola todos los números comprendidos
# * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
# *
# * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
# */
#

# Aritméticos
print("Aritméticos")
print(f"Suma: 2 + 3 = {2 + 3}")
print(f"Resta: 2 - 3 = {2 - 3}")
print(f"Multiplicación: 2 * 3 = {2 * 3}")
print(f"División: 2 / 3 = {2 / 3}")
print(f"División entera: 2 // 3 = {2 // 3}")
print(f"Resto: 2 % 3 = {2 % 3}")
print(f"Potencia: 2 ** 3 = {2**3}")
print()

# lógicos
print("Lógicos")
print(f"AND: True and False = {True and False}")
print(f"OR: True or False = {True or False}")
print(f"NOT: not True = {not True}")
print()

# de comparación
print("De comparación")
print(f"Igual: 2 == 3 = {2 == 3}")
print(f"No igual: 2 != 3 = {2 != 3}")
print(f"Mayor que: 2 > 3 = {2 > 3}")
print(f"Menor que: 2 < 3 = {2 < 3}")
print(f"Mayor o igual que: 2 >= 3 = {2 >= 3}")
print(f"Menor o igual que: 2 <= 3 = {2 <= 3}")
print()

print("De asignación")
a = 2
a += 3
print(f"Suma: a += 3; a = {a}")
a -= 3
print(f"Resta: a -= 3; a = {a}")
a *= 3
print(f"Multiplicación: a *= 3; a = {a}")
a /= 3
print(f"División: a /= 3; a = {a}")
a //= 3
print(f"División entera: a //= 3; a = {a}")
a %= 3
print(f"Resto: a %= 3; a = {a}")
a **= 3
print()

# de identidad
print("De identidad")
obj1 = {0: "a", 1: "b", 2: "c"}
obj2 = {3: "A", 4: "B", 5: "C"}
obj3 = obj1
print(f"obj1 is obj2: {obj1 is obj2}")
print(f"obj1 is not obj2: {obj1 is not obj2}")
print(f"obj1 is obj3: {obj1 is obj3}")
print()

# de pertenencia
print("De pertenencia")
lista: list = [1, 2, 3, 4, 5]
print(f"2 in lista: {2 in lista}")
print(f"6 not in lista: {6 not in lista}")
print()

# de bits
print("De bits")
print(f"AND: 2 & 3 = {2 & 3}")
print(f"OR: 2 | 3 = {2 | 3}")

# Estructuras de control
# Condicionales
print("Condicionales")
if 2 > 3:
    print("2 es mayor que 3")
elif 2 < 3:
    print("2 es menor que 3")
else:
    print("2 es igual a 3")

# iterativas
# for
print("Iterativas")
for i in range(1, 11):
    print(i)

# while
i = 1
while i < 11:
    print(i)
    i += 1

# excepciones

try:
    print(2 / 0)
except ZeroDivisionError:
    print("No se puede dividir por 0")
finally:
    print("Fin del programa")

# DIFICULTAD EXTRA
print("DIFICULTAD EXTRA")
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
