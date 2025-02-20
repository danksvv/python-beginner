# Description: This is a simple program that prints a greeting message
#
# Estas funciones y métodos son esenciales para manipular cadenas en Python.
# Te permiten realizar operaciones comunes como búsqueda, reemplazo, división,
# unión, formateo, y verificación de propiedades. Dominar estas herramientas
# te ayudará a trabajar de manera más eficiente con texto en Python.
#
# Numbers & types

# number01 = int(input("Enter a number: "))
# number02 = int(input("Enter another number: "))
# number03 = int(input("Enter a third number: "))
#
# print(max(number01, number02, number03))
# print(min(number01, number02, number03))
#
# print(type(number01) is int)
# print(type(number01) is str)

# ========================
#
# Sequence types
#
phrase = "Hello Python this is a new project, with new characters"

print(phrase.upper())  # HELLO PYTHON THIS IS A NEW PROJECT
print(phrase.lower())  # hello python this is a new project
print(phrase.capitalize())  # Hello python this is a new project
print(phrase.title())  # Hello Python This Is A New Project
print(phrase.swapcase())  # hELLO pYTHON THIS IS A NEW PROJECT
print(len(phrase))  # 35

# .strip() removes leading and trailing whitespaces
# .lstrip() removes leading whitespaces
# .rstrip() removes trailing whitespaces

print(phrase.replace("Python", "Java"))  # Hello Java this is a new project
print(phrase.split())
# ['Hello', 'Python', 'this', 'is', 'a', 'new', 'project']
print(phrase.split("a"))
# ['Hello Python this is ', ' new project'] # split by "a"
print(",".join(phrase))  # Hello Python this is a new project
print(phrase.index("new"))  # 23
print(phrase.find("new"))  # 23
print(phrase.find("hola"))  # 23
print(phrase.count("new"))  # 2
print(phrase.startswith("Hello"))  # true
print(phrase.endswith("project"))  # false

# .isalpha() returns true if all characters are alphabetic
# .isalnum() returns true if all characters are alphanumeric
# .isdigit() returns true if all characters are isdigit
# .islower() returns true if all characters are lowercase
# .isupper() returns true if all characters are uppercase
#
word = "Hello"
print(word.zfill(10))  # 00000Hello # fill with zeros
print("HELLO ,{}".format(word))  # HELLO ,Hello

# f-strings (formatted string literals)
print(f"Hello, {word}")  # Hello, Hello
# .encode() returns an encoded version of the string
# .decode() returns a decoded version of the string
# .center() returns a centered string
print(word.center(20, "-"))  # -------Hello-------- # center with "-"
