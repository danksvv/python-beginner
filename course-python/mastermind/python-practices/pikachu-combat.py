from random import randint
import sys as system
import time
import os


def printer_effect(effect: str) -> None:
    for letter in effect:
        system.stdout.write(letter)
        system.stdout.flush()
        time.sleep(0.05)
    print()


# function to print the information of the selected
# Pokemon with effects of typing
def info_pokemon(character: str) -> None:
    if character == "a":
        info = (
            "Pikachu is an Electric-type Pokemon.\n"
            "and has the following attacks:\n"
            "1. Thunderbolt ⚡️ \n"
            "2. Quick Attack 🔥 \n"
            "3. Thunder Shock 💥 \n"
        )
        printer_effect(info)

    else:
        info = (
            "Squirtle is a Water-type Pokemon.\n"
            "and has the following attacks:\n"
            "1. Water Gun 💦 \n"
            "2. Bubble Beam 🌊 \n"
            "3. Hydro Pump 🌪 \n"
        )
        printer_effect(info)


# function to select the Pokemon and return the character selected
def select_pokemon() -> str:
    while True:
        character = input(
            "\n [a] Pikachu\n [b] Squirtle\n Select your Pokemon (a or b): "
        )

        if character == "a":
            print("You selected Pikachu!")
            return character
        elif character == "b":
            print("You selected Squirtle!")
            return character
        else:
            print("Invalid option, please try again.")


# function to select the attack of Pikachu and return the damage
def pikachu_attack() -> int:
    attack = 0
    while attack not in [1, 2, 3]:
        attack = input("Select an attack: ")
        match attack:
            case "1":
                print("Pikachu uses Thunderbolt!")
                return 12
            case "2":
                print("Pikachu uses Quick Attack!")
                return 24
            case "3":
                print("Pikachu uses Thunder Shock!")
                return 8
            case _:
                print("Invalid option, please try again.")
    return 0


# function to select the attack of Squirtle and return the damage
def squirtle_attack() -> int:
    attack = 0
    while attack not in [1, 2, 3]:
        attack = input("Select an attack: ")
        match attack:
            case "1":
                print("Squirtle uses Water Gun!")
                return 18
            case "2":
                print("Squirtle uses Bubble Beam!")
                return 6
            case "3":
                print("Squirtle uses Hydro Pump!")
                return 14
            case _:
                print("Invalid option, please try again.")
    return 0


def random_attack(character: str) -> int:
    if character == "a":
        attack_squirtle_list = [18, 6, 8]
        damage = attack_squirtle_list[randint(0, 2)]
    else:
        attack_pikachu_list = [12, 8, 2]
        damage = attack_pikachu_list[randint(0, 2)]
    return damage


def main() -> None:
    pikachu_hp: int = 120
    squirtle_hp: int = 120

    os.system("clear")

    printer_effect("Pokemon Battle: Pikachu vs Squirtle")
    printer_effect("The battle begins!")
    character = select_pokemon()
    info_pokemon(character)

    while pikachu_hp > 0 and squirtle_hp > 0:
        print(f"Squirtle's HP: {squirtle_hp}")
        print(f"Pikachu's HP: {pikachu_hp}")

        if character == "a":
            hurt = pikachu_attack()
            squirtle_hp -= hurt

            printer_effect("Now it's my turn! Squirtle uses an attack!\n")
            pikachu_hp -= random_attack(character)

        else:
            hurt = squirtle_attack()
            pikachu_hp -= hurt

            printer_effect("Now it's my turn! Pikachu uses an attack!\n")
            squirtle_hp -= random_attack(character)

    if pikachu_hp > 0:
        printer_effect("Pikachu wins!")
    else:
        printer_effect("Squirtle wins!")


if __name__ == "__main__":
    main()
