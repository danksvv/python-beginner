# check always of type value, this make sure that the value is always of type of reference 

# this is ok, but not recommended, because this value can be changed by other type of value for example float ❌
number1 = 10 


# this is recommended, because this value can't be changed by other type of value ✅
number2: int = 10 

# in this list we can have any type of value, this is not recommended ❌
# def upper_everything(elements):
#     return [element.upper() for element in elements]

# in this list we can have only strings, this is recommended ✅
def upper_everything(elements: list[str]) -> list[str]:
    return [element.upper() for element in elements]

def main() -> None:
    loud_list: list[str] = upper_everything(["hello", "world"])
    print(loud_list)

if __name__ == "__main__":
    main()
