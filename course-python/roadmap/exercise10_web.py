# web navigation with a stack
#


def web_navigation_with_stack():
    stack: list = []
    while True:
        command = input("Enter 'back' to go back, 'exit' to quit, or a URL to visit: ")
        if command == "back":
            if stack:
                print(f"Going back to {stack.pop()}")
            else:
                print("No previous pages.")
        elif command == "exit":
            break
        else:
            stack.append(command)
            print(f"Visiting {command}")


def shared_printer():
    queue: list = []
    while True:
        command = input(
            "Enter 'print' to print the next item, 'exit' to quit, or an item to add: "
        )
        if command == "print":
            if queue:
                print(f"Printing {queue.pop(0)}")
            else:
                print("No items to print.")
        elif command == "exit":
            break
        else:
            queue.append(command)
            print(f"Added {command} to the queue.")


def main():
    # web_navigation_with_stack()
    shared_printer()


if __name__ == "__main__":
    main()
