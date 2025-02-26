# Description: This program is a simple example of a decision tree
# that helps you choose a mobile phone based on your preferences.
def haveMoney():
    print("You have enough money to buy the mobile phone.")
    print("a) yes" + "\n" + "b) no" + "\n")
    money = input("Do you want to buy the mobile phone? (a/b): ")
    if money == "a":
        return True
    elif money == "b":
        return False
    else:
        print("Invalid option")
        exit()

# Function to choose if you want a mobile phone with a camera


def withCamera():
    print("You have chosen a mobile phone with a camera.")
    print("a) yes" + "\n" + "b) no" + "\n")
    camera = input("Do you want a mobile phone with a camera? (a/b): ")
    if camera == "a":
        return True
    elif camera == "b":
        return False
    else:
        print("Invalid option")
        exit()


# Main program

title = "Welcome at your buy of a new mobile phone!"
print(title + "\n" + "="*len(title) + "\n")
print("a) Iphone" + "\n" + "b) Android" + "\n")
system_mobile = input("Choose the system of your new mobile phone (a/b): ")

if system_mobile == "a" or system_mobile == "A":
    print("You have chosen an Iphone.")
    if haveMoney():
        print("Can you buy Iphone 12 Pro Max")
    else:
        print("Can you buy iPhone of second hand")
elif system_mobile == "b" or system_mobile == "B":
    print("You have chosen an Android.")
    if haveMoney():
        # print("Can you buy Samsung Galaxy S21 Ultra")
        if withCamera():
            print("Can you buy a Google Pixel 5")
        else:
            print("Can you buy any Android mobile phone")
    else:
        print("Can you buy Samsung Galaxy of second hand")
else:
    print("Invalid option")

exit()
