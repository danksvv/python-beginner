# methods for sets in python
#
# SET is a collection which is unordered and unindexed. No duplicate members.
# esto significa que no se puede acceder a los elementos
# de un set por su indice
# y no se pueden tener elementos duplicados en un set.
# son muy utiles para hacer operaciones de conjuntos como union,
# interseccion, diferencia, etc.
# characteristics: unordered, unindexed, no duplicate members.
#
# methods:

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  # create a set
print(my_set)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]  # create a list
print(set(lista))  # convert a list to a set, elimina los elementos duplicados

# add an element to the set (no se puede agregar un elemento duplicado)
my_set.add(11)
my_set.add(11)
print(my_set)  # only print one 11

# remove an element from the set
my_set.remove(11)
print(my_set)

# discard an element from the set (no genera error si el elemento no existe)
my_set.discard(5)
print(my_set)

# pop borra un elemento aleatorio del set
my_set.pop()
print(my_set)

# clear() borra todos los elementos del set
my_set.clear()
print(my_set)

set1 = {1, 2, 3, 4, 5, 8}
set2 = {4, 5, 6, 7, 8, 1}

# union() return a set with all the elements from both sets
print(set1.union(set2))
# intersection() return a set with the elements that are in both sets
print(set1.intersection(set2))
# difference() return a set with the elements that are in set1 but not in set2
print(set1.difference(set2))

# symmetric_difference() return a
# set with the elements that are in one of the sets but not in both
# issubset() return True if all
# the elements of a set are in another set
# issuperset() return True if
# all the elements of another set are in a set
