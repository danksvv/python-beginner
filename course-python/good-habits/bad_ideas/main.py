from typing import Any


user_input: Any = "ten"

try:
    print(f"Converting {user_input} to float")
    print(float(user_input))
except (TypeError, ValueError) as e:
    print("Please enter a valid number")
