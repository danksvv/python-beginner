# this way is ok , but not the better way, show you a betters ways to do it
def vowels(text):
    return sum(char.lower() in "aeiou" for char in text)


print(vowels("hello"))  # 2


# Way 1: Using name description for u functions and variables
def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a given text.
    >>> count_vowels("hello") # 2
    :param text: the text to count the vowels in
    :return: the number total vowel count as a integer
    """
    if not isinstance(text, str):
        raise TypeError(f"Please only use strings, {
                        type(text)} is not valid type.")

    vowels_count = 0
    for char in text:
        if char.lower() in "aeiouAEIOU":
            vowels_count += 1

    return vowels_count
    # return sum(char.lower() in "aeiou" for char in text)


def main() -> None:
    text: str = "lorem ipsum dolor sit amet consectetur adipiscing elit"

    print(vowels(text))  # 16
    print(count_vowels(text))  # 16


if __name__ == "__main__":
    main()
