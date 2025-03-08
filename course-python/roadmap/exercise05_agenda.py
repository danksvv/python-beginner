def check_phone_number(phone_number: str) -> bool:
    """Check if the phone number is valid or not"""
    return phone_number.isdigit() and len(phone_number) == 9


def is_agenda_empty(agenda: dict) -> bool:
    """Check if the agenda is empty or not"""
    return len(agenda) == 0


def update_agenda(agenda: dict[str, str], nombre: str, telefono=None) -> dict[str, str]:
    """Update the agenda with a new contact or update an existing contact
    :param agenda: The current agenda
    :param nombre: The name of the contact
    :param telefono: The phone number of the contact
    :return: The updated agenda
    """
    new_agrenda = agenda.copy()
    if telefono is None:
        del new_agrenda[nombre]
    else:
        new_agrenda[nombre] = telefono
    return new_agrenda


def insertar_contacto(agenda: dict[str, str]) -> dict[str, str]:
    nombre = input("Introduce el nombre del contacto: ")
    telefono = input("Introduce el telefono del contacto: ")
    if check_phone_number(telefono):
        print("El telefono debe ser numerico y tener 9 digitos")
        return agenda
    if nombre in agenda:
        print("El contacto ya existe")
        return agenda
    print("Contacto agregado correctamente")
    return update_agenda(agenda, nombre, telefono)


def search_contact(agenda: dict):
    """Search a contact in the agenda by name"""
    if is_agenda_empty(agenda):
        print("Agenda vacia")
        return agenda
    else:
        nombre = input("Introduce el nombre del contacto: ")
        if nombre in agenda:
            print(f"El telefono de {nombre} es {agenda[nombre]}")
        else:
            print("Contacto no encontrado")


def update_contact(agenda: dict[str, str]) -> dict[str, str]:
    """Update a contact in the agenda"""
    if is_agenda_empty(agenda):
        print("Agenda vacia")
        return agenda
    nombre = input("Introduce el nombre del contacto: ")
    if nombre in agenda:
        nuevo_telefono = input("Introduce el nuevo telefono del contacto: ")
        if check_phone_number(nuevo_telefono):
            print("El telefono debe ser numerico y tener 9 digitos")
            return agenda
        print("Contacto actualizado correctamente")
        return update_agenda(agenda, nombre, nuevo_telefono)
    else:
        print("Contacto no encontrado")
        return agenda


def delete_contact(agenda: dict[str, str]) -> dict[str, str]:
    """Delete a contact from the agenda"""
    if len(agenda) == 0:
        print("Agenda vacia")
        return agenda
    else:
        nombre = input("Introduce el nombre del contacto: ")
        if nombre in agenda:
            print("Contacto eliminado correctamente")
            return update_agenda(agenda, nombre)
        else:
            print("Contacto no encontrado")
        return agenda


def show_all_contacts(agenda: dict):
    """Show all the contacts in the agenda"""
    if is_agenda_empty(agenda):
        print("Agenda vacia")
        return agenda
    else:
        print("\n--- Contactos ---")
        for nombre, telefono in agenda.items():
            print(f"{nombre} - {telefono}")
        print("------------------\n")


def main():
    agenda = {}

    while True:
        print("Welcome at you agenda")
        print("1. Insertar contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos los contactos")
        print("6. Salir")
        option = input("Introduce una opcion: ")

        if option == "1":
            agenda = insertar_contacto(agenda)
        elif option == "2":
            search_contact(agenda)
        elif option == "3":
            agenda = update_contact(agenda)
        elif option == "4":
            agenda = delete_contact(agenda)
        elif option == "5":
            show_all_contacts(agenda)
        elif option == "6":
            print("gracias por usar la agenda, nos vemos pronto!")
            break
        else:
            print("Opcion no valida por favor introduce una opcion valida")


if __name__ == "__main__":
    main()
