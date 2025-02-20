def main() -> None:
    people: list[str] = ["Jackeline", "John", "Jane", "Joe", "Jill", "Jack", "Jen"]

    # this way is very long, you can make it shorter and more readable 😵
    # long_names: list[str] = []
    #
    # for person in people:
    #     if len(person) > 7:
    #         long_names.append(person)
    #
    # print(long_names)

    # this way is shorter and more readable 😎
    long_names: list[str] = [person for person in people if len(person) > 7]

    print(f"Long names: {long_names}")


if __name__ == "__main__":
    main()
