# this not is a good practice ❌ 
# def enter_club(name:str, age:int, has_id:bool) -> None:
#     if name.lower() == "bob": 
#         print("Get out of here Bob!, we don\'t want not trouble.")
#         return 
#
#     if age > 21 and has_id:
#         print("Welcome to the club!")
#     else:
#         print("You are not allowed to enter the club.")

# the best practice is define every condition in a separate function ✅
def is_an_adult(age:int, has_id:bool) -> bool:
    return age >= 21 and has_id


def is_bob(name:str) -> bool:
    return name.lower() == "bob"


def enter_club(name:str, age:int, has_id:bool) -> None:
    if is_bob(name):
        print(f"Get out of here {name}!, we don\'t want not trouble.")
        return 

    if is_an_adult(age, has_id):
        print(f"Welcome to the club {name}!")
    else:
        print("You are not allowed to enter the club.")


def main() -> None:
    enter_club("Bob", 22, True)
    enter_club("Alice", 22, False)
    enter_club("Jorge", 23, True)
    enter_club("Virginia", 15, True)
    enter_club("Sara", 35, True)


if __name__ == "__main__":
    main()
