# list with all the methods for python
# son colecciones ordenadas y mutables de elementos,
# y se definen con llaves {} y con elementos separados por comas.
# contienen elementos de diferentes tipos y no tienen un tamaño fijo.
# characteristics: ordered, mutable, no duplicate members.
#
# methods:
#
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # create a list

print(my_list)
# append() add an element to the end of the list
my_list.append(11)
print(my_list)

# extend() add the elements of a list (or any iterable) to the end of the list
my_list_extend = [12, 13, 14]
my_list.extend(my_list_extend)

print(my_list)

# insert() add an element at a specific position
my_list.insert(0, 0)  # add 0 the list , in this case at position 0
print(my_list)

# remove() remove an element from the list
# (if the element does not exist, it generates an error)
my_list.remove(0)
print(my_list)

# pop() remove the element at the end of the list (if the index is specified,
# it removes the element at that index)
my_list.pop()
print(my_list)

# clear() remove all the elements from the list
my_list.clear()
print(my_list)

# index() return the index of the first element with the specified value
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4, 5, 6]
print(my_list.index(5))

# count() return the number of elements with the specified ValueError
print(my_list.count(5))

# sort() sort the list
my_list.sort()
print(my_list)

# reverse() reverse the order of the list
my_list.reverse()
print(my_list)

# copy() return a copy of the list
my_list_copy = my_list.copy()

print(my_list_copy)

#  concatenation
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]

my_list3 = my_list1 + my_list2
print(my_list3)

# repetition
my_list4 = my_list1 * 3
print(my_list4)

# slice
my_list5 = my_list1[1:3]
print(my_list5)

# check if an element is in the list
print(1 in my_list1)
print(7 in my_list1)

# change list of chains to uppercase
frutas = ["manzana", "banana", "cereza"]
frutas_mayusculas = [fruta.upper() for fruta in frutas]
print(frutas_mayusculas)  # Salida: ['MANZANA', 'BANANA', 'CEREZA']
