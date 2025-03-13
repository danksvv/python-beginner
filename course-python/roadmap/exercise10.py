# /*
# * EJERCICIO:
# * Implementa los mecanismos de introducción y recuperación de elementos propios de las
# * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
# * o lista (dependiendo de las posibilidades de tu lenguaje).
# *
# * DIFICULTAD EXTRA (opcional):
# * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
# *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
# *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
# *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
# *   el nombre de una nueva web.
# * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
# *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
# *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
# *   interpretan como nombres de documentos.
# */


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None


# Example usage:
def main():
    # Stack example
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())  # Output: 3
    print(stack.peek())  # Output: 2

    # Queue example
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())  # Output: 1
    print(queue.peek())  # Output: 2


if __name__ == "__main__":
    main()
