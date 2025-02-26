from collections import ChainMap

# two dictionaries
# dict1: dict[str, int] = {"a": 1, "b": 2}
# dict2: dict[str, int] = {"b": 3, "c": 4}
#
# print(dict1 | dict2)  # {'a': 1, 'b': 3, 'c': 4}
#
# cm: ChainMap[str, int] = ChainMap(dict1, dict2)
#
# # create a single view of the dictionaries
# print(cm)  # ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
#
# cm: ChainMap[str, int] = cm.new_child({"d": 5, "e": 6})
# print(cm)  # ChainMap({'d': 5, 'e': 6}, {'a': 1, 'b': 2}, {'b': 3, 'c': 4})
#
# names: list[str] = ["Alice", "Bob", "Charlie"]
# cm2: ChainMap[str, None] = ChainMap.fromkeys(names, None)
# print(cm2)  # ChainMap({'Alice': None, 'Bob': None, 'Charlie': None})
#
# cm2.update({"David": None})
# print(cm2)  # ChainMap({'Alice': None, 'Bob': None, 'Charlie': None, 'David': None})

# example in a case practical
# define preferences of a user, with two dictionaries, one for the default preferences and another for the user preferences

default_settings: dict[str, str | bool] = {
    "theme": "light",
    "language": "English",
    "show_notifications": True,
}

user_settings: dict[str, str | bool] = {
    "theme": "dark",
    "show_notifications": False,
}

# create a ChainMap with the default settings and the user settings
preferences: ChainMap[str, str | bool] = ChainMap(
    user_settings, default_settings)
print(
    preferences
)  # ChainMap({'theme': 'dark', 'show_notifications': False}, {'theme': 'light', 'language': 'English', 'show_notifications': True})
