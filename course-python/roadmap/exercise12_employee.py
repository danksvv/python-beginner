# * DIFICULTAD EXTRA (opcional):
# * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
# * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
# * Cada empleado tiene un identificador y un nombre.
# * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
# * actividad, y almacenan los empleados a su cargo.


class Employee:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(f"{self.name} has {employee.name} employee.")


class Manager(Employee):
    def coordinate_projects(self):
        print(f"{self.name} is coordinating projects.")


class ProjectManager(Employee):
    def __init__(self, id: int, name: str, projects: list):
        super().__init__(id, name)
        self.projects = projects

    def coordinate_project(self):
        print(f"{self.name} is coordinating his project.")


class Programmer(Employee):
    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} is coding in {self.language}.")

    def add_employee(self, employee: Employee):
        print(f"{self.name} is not a manager, he can't add  {employee.name} employee.")


def main():
    my_manager: Manager = Manager(1, "John")
    my_project_manager: ProjectManager = ProjectManager(
        2, "Jane", ["Project A", "Project B"]
    )
    my_project_manager2: ProjectManager = ProjectManager(
        3, "Jill", ["Project C", "Project D"]
    )
    my_programmer: Programmer = Programmer(3, "Alice", "Python")
    my_programmer2: Programmer = Programmer(4, "Bob", "Java")
    my_programmer3: Programmer = Programmer(5, "Charlie", "C++")
    my_programmer4: Programmer = Programmer(6, "David", "JavaScript")

    my_project_manager.add_employee(my_programmer)
    my_project_manager.add_employee(my_programmer2)

    my_project_manager2.add_employee(my_programmer3)
    my_project_manager2.add_employee(my_programmer4)

    my_manager.add_employee(my_project_manager)

    my_programmer.add_employee(my_programmer2)

    my_manager.coordinate_projects()

    my_project_manager.coordinate_project()

    my_project_manager2.print_employees()


if __name__ == "__main__":
    main()
