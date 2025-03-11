# /*
# * EJERCICIO:
# * Entiende el concepto de recursividad creando una función recursiva que imprima
# * números del 100 al 0.
# *
# * DIFICULTAD EXTRA (opcional):
# * Utiliza el concepto de recursividad para:
# * - Calcular el factorial de un número concreto (la función recibe ese número).
# * - Calcular el valor de un elemento concreto (según su posición) en la
# *   sucesión de Fibonacci (la función recibe la posición).
# */


# def printNumbers(n):
#     if n < 0:
#         return
#     print(n)
#     printNumbers(n - 1)
#
#
# printNumbers(100)
#
# factorial


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(f"Factorial de 5: {factorial(5)}")


# Fibonacci


def fibonacci(n):
    """Initialize the first two numbers of the sequence"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        """destructuring assignment"""
        a, b = b, a + b


print(list(fibonacci(10)))
