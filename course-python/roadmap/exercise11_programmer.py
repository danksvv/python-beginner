class Programmer:
    def __init__(self, name: str, age: int, language: list):
        self.name = name
        self.age = age
        self.language = language

    def print_programmer(self):
        print(f"Name: {self.name}, Age: {
              self.age}, Languages: {self.language}")


def main():
    programmer1: Programmer = Programmer(
        "Alice", 25, ["Python", "Java", "C++"])
    programmer2: Programmer = Programmer(
        "Bob", 30, ["Python", "C#", "JavaScript"])
    print("Programmer 1:")
    programmer1.print_programmer()
    print("Programmer 2:")
    programmer2.print_programmer()


if __name__ == "__main__":
    main()
