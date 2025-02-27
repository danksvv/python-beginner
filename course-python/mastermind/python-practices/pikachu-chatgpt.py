import os
import sys as system
import time
from random import choice

# Constants for HP and attack damage
INITIAL_HP = 120
PIKACHU_ATTACKS = {
    "1": ("Thunderbolt ⚡️", 12),
    "2": ("Quick Attack 🔥", 24),
    "3": ("Thunder Shock 💥", 8),
}
SQUIRTLE_ATTACKS = {
    "1": ("Water Gun 💦", 18),
    "2": ("Bubble Beam 🌊", 6),
    "3": ("Hydro Pump 🌪", 14),
}


def printer_effect(effect: str, delay: float = 0.05) -> None:
    """Prints text with a typing effect."""
    for letter in effect:
        system.stdout.write(letter)
        system.stdout.flush()
        time.sleep(delay)
    print()


def info_pokemon(character: str) -> None:
    """Prints Pokémon info with attacks."""
    info = {
        "a": "Pikachu is an Electric-type Pokémon.\nIt has the following attacks:\n"
        "1. Thunderbolt ⚡️ (12 dmg)\n2. Quick Attack 🔥 (24 dmg)\n3. Thunder Shock 💥 (8 dmg)\n",
        "b": "Squirtle is a Water-type Pokémon.\nIt has the following attacks:\n"
        "1. Water Gun 💦 (18 dmg)\n2. Bubble Beam 🌊 (6 dmg)\n3. Hydro Pump 🌪 (14 dmg)\n",
    }
    printer_effect(info.get(character, "Invalid Pokémon!"))


def select_pokemon() -> str:
    """Asks the player to select a Pokémon."""
    while True:
        character = input(
            "\n[a] Pikachu\n[b] Squirtle\nSelect your Pokémon (a or b): "
        ).lower()
        if character in ["a", "b"]:
            print(f"You selected {'Pikachu' if character == 'a' else 'Squirtle'}!")
            return character
        print("Invalid option, please try again.")


def select_attack(attacks: dict) -> int:
    """Asks the player to choose an attack and returns its damage."""
    while True:
        attack = input("Select an attack: ")
        if attack in attacks:
            print(f"{attacks[attack][0]}!")
            return attacks[attack][1]
        print("Invalid option, please try again.")


def random_attack(attacks: dict) -> int:
    """Selects a random attack from the opponent."""
    attack_name, damage = choice(list(attacks.values()))
    print(f"The opponent uses {attack_name}!")
    return damage


def life_bar(hp: int, total_hp: int = INITIAL_HP) -> str:
    """Creates a life bar based on the percentage of HP left."""
    bar_length = 10
    filled = int((hp / total_hp) * bar_length)
    return f"[{'♥' * filled}{' ' * (bar_length - filled)}] {hp}/{total_hp} HP"


def main() -> None:
    """Main function that runs the game."""
    pikachu_hp, squirtle_hp = INITIAL_HP, INITIAL_HP

    os.system("clear")

    printer_effect("⚡️ Pokémon Battle: Pikachu vs Squirtle 🌊")
    printer_effect("The battle begins!")
    character = select_pokemon()
    info_pokemon(character)

    while pikachu_hp > 0 and squirtle_hp > 0:
        print("\nSquirtle's HP:", life_bar(squirtle_hp))
        print("Pikachu's HP:", life_bar(pikachu_hp))

        if character == "a":
            squirtle_hp -= select_attack(PIKACHU_ATTACKS)
            if squirtle_hp <= 0:
                break
            printer_effect("Now it's the opponent's turn!\n")
            pikachu_hp -= random_attack(SQUIRTLE_ATTACKS)
        else:
            pikachu_hp -= select_attack(SQUIRTLE_ATTACKS)
            if pikachu_hp <= 0:
                break
            printer_effect("Now it's the opponent's turn!\n")
            squirtle_hp -= random_attack(PIKACHU_ATTACKS)

    winner = "Pikachu" if pikachu_hp > 0 else "Squirtle"
    printer_effect(f"🎉 {winner} wins! 🎉")


if __name__ == "__main__":
    main()
