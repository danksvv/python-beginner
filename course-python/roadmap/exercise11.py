# /*
# * EJERCICIO:
# * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
# * atributos y una función que los imprima (teniendo en cuenta las posibilidades
# * de tu lenguaje).
# * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
# * utilizando su función.
# *
# * DIFICULTAD EXTRA (opcional):
# * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
# * en el ejercicio número 7 de la ruta de estudio)
# * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
# *   retornar el número de elementos e imprimir todo su contenido.
# *
# */
#


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

    def print_stack(self):
        print(self.stack)


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

    def print_queue(self):
        print(self.queue)


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_stack()
    print(stack.pop())
    stack.print_stack()
    print(stack.pop())
    stack.print_stack()
    print(stack.pop())
    stack.print_stack()
    print(stack.pop())
    stack.print_stack()

    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.print_queue()
    print(queue.pop())
    queue.print_queue()
    print(queue.pop())
    queue.print_queue()
    print(queue.pop())
    queue.print_queue()
    print(queue.pop())
    queue.print_queue()


if __name__ == "__main__":
    main()
