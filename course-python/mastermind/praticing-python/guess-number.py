# program to guess a number between 1 and 100

import random


def obtener_numero(mensaje):
    while True:
        entrada = input(mensaje)  # Solicita la entrada al usuario
        try:
            numero = float(entrada)
            # Intenta convertir la entrada a un número (float o int)
            # Usamos float para aceptar tanto enteros como decimales
            if numero.is_integer():  # Si es un entero, lo convertimos a int
                numero = int(numero)
                if numero < 1 or numero > 10:
                    # Si el número no está en el rango, muestra un mensaje
                    print("Error: Debes ingresar un número entre 1 y 10.")
                    continue
            return numero  # Retorna el número válido
        except ValueError:
            # Si ocurre un error, muestra un mensaje personalizado
            print("Error: Debes ingresar un número válido.Inténtalo de nuevo.")

# inicio del programa


print("Welcome to the number guessing game!")

enter_number = obtener_numero("Enter a number between 1 to 10: ")

random_number = random.randint(1, 10)

count = 1

while True:
    if enter_number == random_number:
        print(f"Congratulations! You guessed the number in {count} tries.")
        break
    elif count == 3:
        print("Sorry, you have reached the maximum number of tries.")
        print(f"The number was {random_number}.")
        break
    elif enter_number < random_number:
        enter_number = obtener_numero("Try again. Enter a higher number: ")
    else:
        enter_number = obtener_numero("Try again. Enter a lower number: ")
    count += 1
