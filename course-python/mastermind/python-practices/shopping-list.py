"""
program to create a shopping list
"""

import os


# function to add an item to the shopping list
def add_item(shopping_list: list[str]) -> list[str]:
    item = input("Enter the item to add: ")
    if item not in shopping_list:
        shopping_list.append(item)
    else:
        print("Item already in the shopping list.")
    return shopping_list


# function to remove an item from the shopping list:
def remove_item(shopping_list: list[str]) -> list[str]:
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print("Item not found in the shopping list.")
    return shopping_list


# function to display the shopping list:
def display_list(shopping_list: list[str]) -> None:
    os.system("clear")
    print("Shopping List:\n")
    for item in shopping_list:
        print(f"- {item}")
    print()


def main() -> None:
    shopping_list = []
    message = "Shopping List"
    os.system("clear")

    while True:
        print("*" * len(message))
        print("Shopping List")
        print("*" * len(message))

        print("\n1. Add item")
        print("2. Remove item")
        print("3. Display list")
        print("4. Exit")
        option = input("Select an option: ")
        if option == "1":
            shopping_list = add_item(shopping_list)
        elif option == "2":
            shopping_list = remove_item(shopping_list)
        elif option == "3":
            display_list(shopping_list)
        elif option == "4":
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
