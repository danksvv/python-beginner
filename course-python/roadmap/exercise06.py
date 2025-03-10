# /*
# * EJERCICIO:
# * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
# * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
# * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
# *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
# *
# * DIFICULTAD EXTRA (opcional):
# * Crea un programa que analice dos palabras diferentes y realice comprobaciones
# * para descubrir si son:
# * - Palíndromos
# * - Anagramas
# * - Isogramas
# */

# cadenas en python
# metodos de cadenas en python
# 1. Acceso a caracteres específicos
print("Acceso a caracteres específicos:\n")
cadena = input("Introduce una cadena: ")

print(f"El primer caracter de la cadena es: {cadena[0]}")
print(f"El ultimo caracter de la cadena es: {cadena[-1]}")

# 2. subcadenas
print("\nSubcadenas:\n")
print(f"Los tres primeros caracteres de la cadena son: {cadena[:3]}")
print(f"Los tres ultimos caracteres de la cadena son: {cadena[-3:]}")
print(f"Los caracteres de la cadena en posiciones pares son: {cadena[::2]}")
print(f"Los caracteres de la cadena en posiciones impares son: {cadena[1::2]}")
print(f"La cadena al reves es: {cadena[::-1]}")
print(f"La cadena al reves de 2 en 2 es: {cadena[::-2]}")

# 3. longitud
print("\nLongitud:\n")
print(f"La longitud de la cadena es: {len(cadena)}")
print(f"La longitud de la cadena sin espacios es: {
      len(cadena.replace(' ', ''))}")

# 4. concatenación
print("\nConcatenación:\n")
cadena2 = input("Introduce otra cadena: ")
print(f"La concatenación de las dos cadenas es: {cadena, ' ', cadena2}")
concatenacion = cadena + " " + cadena2
print(f"La concatenación de las dos cadenas es: {concatenacion}")

# 5. repetición
print("\nRepetición:\n")
print(f"La cadena repetida 3 veces es: {cadena * 3}")

# 6. recorrido
print("\nRecorrido:\n")
for i in cadena:
    print(i)

# 7. conversión a mayúsculas y minúsculas
print("\nConversión a mayúsculas y minúsculas:\n")
print(f"La cadena en mayúsculas es: {cadena.upper()}")
print(f"La cadena en minúsculas es: {cadena.lower()}")

# 8. reemplazo
print("\nReemplazo:\n")
texto = "Hola mundo"
print(f"La cadena original es: {texto}")
cadena3 = input("Introduce una cadena para reemplazar: ")
cadena4 = input("Introduce una cadena para reemplazar: ")
cadena_reemplazo = texto.replace(cadena3, cadena4)
print(f"La cadena reemplazada es: {cadena_reemplazo}")

# 9. división
print("\nDivisión:\n")
cadena5 = input("Introduce una cadena con espacios: ")
cadena_dividida = cadena5.split()
print(f"La cadena dividida es: {cadena_dividida}")
print(f"La cadena dividida con un limite de 2 es: {cadena5.split(' ', 2)}")
print(type(cadena_dividida))

# 10. unión
print("\nUnión:\n")
cadena6 = input("Introduce una cadena: ")
cadena7 = input("Introduce otra cadena: ")
cadena_unida = " ".join([cadena6, cadena7])
print(f"La cadena unida es: {cadena_unida}")

# 11. interpolación
# La interpolación de cadenas es una técnica para incluir valores dentro
# de una cadena de manera más legible y eficiente que la concatenación (+).
print("\nInterpolación:\n")
nombre = "Juan"
edad = 25
print(f"Hola, me llamo {nombre} y tengo {edad} años")

# 12. verificación
print("\nVerificación:\n")
cadena8 = input("Introduce una cadena: ")
print(f"La cadena es alfanumerica: {cadena8.isalnum()}")
print(f"La cadena es alfabetica: {cadena8.isalpha()}")
print(f"La cadena es numerica: {cadena8.isnumeric()}")
print(f"La cadena es minusculas: {cadena8.islower()}")
print(f"La cadena es mayusculas: {cadena8.isupper()}")
print(f"La cadena es decimal: {cadena8.isdecimal()}")
print(f"La cadena es un espacio: {cadena8.isspace()}")
