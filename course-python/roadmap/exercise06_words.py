import os
import platform


# function to clear the screen
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# function to check if a word is a palindrome
def enter_word() -> str:
    while True:
        text = input("Enter a word: ")
        if text:
            return text
        print("Input can't be empty, Please try again")


# function to check if a word is a palindrome
def is_palindrome(text: str) -> bool:
    text = text.lower().replace(" ", "")
    return text == text[::-1]


# function to check if two words are anagrams
def is_anagram(text1: str, text2: str) -> bool:
    return sorted(text1) == sorted(text2)


# function to check if a word is an isogram
def is_isogram(text: str) -> bool:
    text = text.lower().replace(" ", "")
    return len(text) == len(set(text))


# function to print a line
def line_printer(text: str) -> None:
    print("-" * len(text))


# main menu
def main():
    text = ""
    text2 = ""
    text_entered = False

    while True:
        print("Welcome to the words program\n")
        print("1. Palindrome")
        print("2. Anagrams")
        print("3. Isograms")
        print("4. Exit\n")
        option = input("Select an option: ")

        # only ask for a word if the option is 1, 2 or 3
        if not text_entered and option in ["1", "2", "3"]:
            text = enter_word()
            if option == "2":
                text2 = enter_word()
            text_entered = True

        # print * only if the text variable is not empty
        clear_screen()
        if text_entered:
            line_printer(text)
        if option == "1":
            if is_palindrome(text):
                print(f"{text} is a palindrome")
            else:
                print(f"{text} is not a palindrome")

        elif option == "2":
            if is_anagram(text, text2):
                print(f"{text} and {text2} are anagrams")
            else:
                print(f"{text} and {text2} are not anagrams")

        elif option == "3":
            if is_isogram(text):
                print(f"{text} is an isogram")
            else:
                print(f"{text} is not an isogram")
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option\n")
        # reset the text variable
        if text_entered:
            line_printer(text)
        text_entered = False
        text = ""
        text2 = ""


if __name__ == "__main__":
    main()
