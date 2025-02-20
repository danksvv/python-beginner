def poundsToEuro(amount):
    return round(amount * 1.16, 2)


def eurosToPounds(amount):
    return round(amount / 1.16, 2)


amount = float(input("Enter the amount: "))
badge = input("Enter the currency (p for pounds or e for euros): ")

if badge == "p" or badge == "P":
    print(f"{amount} pounds are {poundsToEuro(amount)} euros")
elif badge == "e" or badge == "E":
    print(f"{amount} euros are {eurosToPounds(amount)} pounds")
else:
    print("Invalid currency")
exit()
