def main():
    dict1: dict = {"Deutschland": "Berlin", "France": "Paris", "Italy": "Rome"}
    dict2: dict = {"Spain": "Madrid", "Portugal": "Lisbon", "France": "Paris"}

    print("dict1: ", dict1)
    print("dict2: ", dict2)

    # add new key-value pair to dict1
    dict1["Spain"] = "Madrid"

    print("dict1: ", dict1)

    # remove key-value pair from dict2
    del dict2["France"]

    print("dict2: ", dict2)

    # combine a tuple and a dictionary
    tuple1: tuple = ("Deutschland", "France", "Italy")
    countries: dict = {tuple1[0]: "Berlin", tuple1[1]: "Paris", tuple1[2]: "Rome"}

    print("countries: ", countries)

    # methods of dictionaries
    #
    # 1 - values() - returns the values of the dictionary
    #
    users: dict = {0: "Alice", 1: "Bob", 2: "Charlie", 3: "David"}
    print(users.values())

    # 2 - keys() - returns the keys of the dictionary
    #
    print(users.keys())

    # 3 = pop() - removes the key-value pair from the dictionary
    #
    popped: str = users.pop(2)
    print(popped)
    print(users)

    # 4 - popitem() - removes the last key-value pair from the dictionary
    #
    popped2: tuple = users.popitem()
    print(popped2)

    # 5 - copy() - returns a copy of the dictionary
    # this copy is a reference to the original dictionary and some changes
    # in the copy will affect the original dictionary and vice versa
    #
    sample_dict: dict = {0: ["a", "b", "c"], 1: ["d", "e", "f"], 2: ["g", "h", "i"]}
    copy_dict: dict = sample_dict.copy()

    print("sample_dict: ", sample_dict)
    print("copy_dict: ", copy_dict)

    # 6 - get() - returns the value of the key passed as argument
    #
    others_users: dict = {0: "Alice", 1: "Bob", 2: "Charlie", 3: "David"}
    print(others_users.get(2))
    print(others_users.get(4))

    # 7 - setdefault() - returns the value of the key passed as argument
    # if the key does not exist, it creates a new key-value pair
    #
    print(others_users.setdefault(2))
    print(others_users.setdefault(4, "Eve"))
    print(others_users)

    # 8 - clear() - removes all key-value pairs from the dictionary
    # and returns an empty dictionary

    others_users.clear()
    print(others_users)

    # 9 - fromkeys() - creates a new dictionary with the keys passed
    # as argument and the value passed as argument
    #
    people: list[str] = ["Alice", "Bob", "Charlie", "David"]
    users: dict = dict.fromkeys(people)
    print(users)

    users: dict = dict.fromkeys(people, 0)
    print(users)

    # 10 - items() - returns a list of tuples with the key-value pairs of the dictionary
    #
    users: dict = {0: "Alice", 1: "Bob", 2: "Charlie", 3: "David"}
    print(users.items())

    for key, value in users.items():
        print(key, value)

    # 11 - update() - updates the dictionary with the key-value pairs of another dictionary
    # or with the key-value pairs of a list of tuples
    #
    users: dict = {0: "Alice", 1: "Bob", 2: "Charlie", 3: "David"}
    others_users: dict = {4: "Eve", 5: "Frank"}

    users.update(others_users)

    print(users)

    # | - union operator - combines two dictionaries

    dict1: dict = {"Deutschland": "Berlin", "France": "Paris", "Italy": "Rome"}
    print(dict1 | {"Spain": "Madrid", "Portugal": "Lisbon"})


if __name__ == "__main__":
    main()
