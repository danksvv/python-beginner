from random import randint
import sys as system
import time


# function to print the information of the selected
# Pokemon with effects of typing
def info_pokemon(character: str) -> None:
    # printer = False
    # info = ""
    if character == "a":
        info = (
            "Pikachu is an Electric-type Pokemon.\n"
            "and has the following attacks:\n"
            "1. Thunderbolt ⚡️ \n"
            "2. Quick Attack 🔥 \n"
            "3. Thunder Shock 💥 \n"
        )
        printer = True

    else:
        info = (
            "Squirtle is a Water-type Pokemon.\n"
            "and has the following attacks:\n"
            "1. Water Gun 💦 \n"
            "2. Bubble Beam 🌊 \n"
            "3. Hydro Pump 🌪 \n"
        )
        printer = True

    if printer:
        for letter in info:
            system.stdout.write(letter)
            system.stdout.flush()
            time.sleep(0.05)
        print()


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


def main() -> None:
    pikachu_hp = 100
    squirtle_hp = 100

    print("Pokemon Battle: Pikachu vs Squirtle")
    print("The battle begins!")
    character = select_pokemon()
    info_pokemon(character)

    while pikachu_hp > 0 and squirtle_hp > 0:
        # Pikachu attacks
        pikachu_attack = randint(1, 50)
        squirtle_hp -= pikachu_attack
        print(
            f"Pikachu attacks with a power of {pikachu_attack} HP, Squirtle has {
                squirtle_hp
            } HP left."
        )

        # Squirtle attacks
        squirtle_attack = randint(1, 50)
        pikachu_hp -= squirtle_attack
        print(
            f"Squirtle attacks with a power of {squirtle_attack} HP, Pikachu has {
                pikachu_hp
            } HP left."
        )

        # input

    if pikachu_hp > squirtle_hp:
        print("Pikachu wins!")
    else:
        print("Squirtle wins!")


if __name__ == "__main__":
    main()
