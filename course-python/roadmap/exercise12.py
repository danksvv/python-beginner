# /*
# * EJERCICIO:
# * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
# * implemente una superclase Animal y un par de subclases Perro y Gato,
# * junto con una función que sirva para imprimir el sonido que emite cada Animal.
# *
# * DIFICULTAD EXTRA (opcional):
# * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
# * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
# * Cada empleado tiene un identificador y un nombre.
# * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
# * actividad, y almacenan los empleados a su cargo.
# */


class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says: Meow!")


def print_sound(animal: Animal):
    animal.make_sound()


def main():
    my_dog: Dog = Dog("Buddy")
    my_cat: Cat = Cat("Whiskers")
    my_dog.make_sound()
    my_cat.make_sound()
    print_sound(my_dog)
    print_sound(my_cat)


if __name__ == "__main__":
    main()
