# tuples are immutable, so we can't change the elements
# of a tuple once it's assigned.
#
# Características principales de las tuplas

# Inmutables: No se pueden modificar después de su creación.
# Ordenadas: Los elementos tienen un orden específico y se acceden por su índice
# Heterogéneas: Pueden contener elementos de diferentes tipos.
# Indexadas: Los elementos se acceden mediante índices (comienzan en 0).
# Eficientes: Son más rápidas que las listas para ciertas operaciones debido a su inmutabilidad.
#
# Métodos de las tuplas
#
mi_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # create a tuple
print(mi_tupla)

# count() return the number of times a specified value appears in the tuple

print(mi_tupla.count(5))

# index() return the index of the first element with the specified value
#
print(mi_tupla.index(5))

tuple1 = (1, 2, 3, 4, 5, 8)
tuple2 = (4, 5, 6, 7, 8, 1)

# tuple1 + tuple2 return a tuple with all the elements from both tuples
print(tuple1 + tuple2)

# concatenation
#
print(tuple1 * 2)

# len() return the number of elements in the tuple
print(len(tuple1))

# slicen() return a tuple with the specified range of elements
print(tuple1[1:4])

# Diferencias clave entre tuplas y listas

# Característica	Tuplas	Listas
# Mutabilidad	Inmutables (no se pueden modificar)	Mutables (se pueden modificar)
# Sintaxis	Usan paréntesis ()	Usan corchetes []
# Rendimiento	Más rápidas para ciertas operaciones	Más lentas que las tuplas
# Uso típico	Almacenar datos inmutables	Almacenar datos mutables
