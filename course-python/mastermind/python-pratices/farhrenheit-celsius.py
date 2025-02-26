# create a program that converts temperatures from Fahrenheit to Celsius
# or from Celsius to Fahrenheit depending on the user's choice.

def fahrenheitToCelcius(temperature):
    celsius = (temperature - 32) * 5.0/9.0
    print(f"The temperature in Celsius is {round(celsius, 2)} Celsius")


def celciusToFahrenheit(temperature):
    fahrenheit = (temperature * 9.0/5.0) + 32
    print(f"The temperature in Fahrenheit is {
          round(fahrenheit, 2)} Fahrenheit")


temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit of the temperature (C or F): ")

if unit == 'C' or unit == 'c':
    fahrenheitToCelcius(temperature)
elif unit == 'F' or unit == 'f':
    celciusToFahrenheit(temperature)
else:
    print("Invalid unit")
    exit()
