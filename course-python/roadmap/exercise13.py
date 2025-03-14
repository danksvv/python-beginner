# /*
# * EJERCICIO:
# * Explora el concepto de manejo de excepciones según tu lenguaje.
# * Fuerza un error en tu código, captura el error, imprime dicho error
# * y evita que el programa se detenga de manera inesperada.
# * Prueba a dividir "10/0" o acceder a un índice no existente
# * de un listado para intentar provocar un error.
# *
# * DIFICULTAD EXTRA (opcional):
# * Crea una función que sea capaz de procesar parámetros, pero que también
# * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
# * corresponderse con un tipo de excepción creada por nosotros de manera
# * personalizada, y debe ser lanzada de manera manual) en caso de error.
# * - Captura todas las excepciones desde el lugar donde llamas a la función.
# * - Imprime el tipo de error.
# * - Imprime si no se ha producido ningún error.
# * - Imprime que la ejecución ha finalizado.
# */

# def main():
#     try:
#         my_number: int = int(input("Enter a number: "))
#         division: float = 10 / my_number
#         print(division)
#     except ZeroDivisionError as e:
#         print(f"Error: {e}")
#
#     except ValueError as e:
#         print(f"Error: {e}")
#
#
# if __name__ == "__main__":
#     main()
#
#

# exception custom
class StrTypeError(Exception):
    pass


def process_params(parameters: list):
    if len(parameters) == 0:
        raise ValueError("No parameters provided")
    elif parameters[1] == 0:
        raise ZeroDivisionError("Division by zero")
    elif len(parameters) > 3:
        raise IndexError("Too many parameters provided")
    elif type(parameters[2]) is not int:
        raise StrTypeError("The third parameter is not an integer")

    print(parameters[2])
    print(parameters[0] / parameters[1])
    print(parameters[2] + 5)


def main():
    try:
        # process_params([])
        # process_params([1, 3, "4"])
        # process_params([2, 0, 5])
        # process_params([2, 1, "hello"])
        # process_params([2, 0, 5, 6, 7])
        process_params([2, 1, 5])

    except ValueError as e:
        print(f"Error: {e}")
    except IndexError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except StrTypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("No errors occurred")
    finally:
        print("Execution finished")


if __name__ == "__main__":
    main()
