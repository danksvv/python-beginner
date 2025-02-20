# functions to work with numbers
#
# import cmath
import math
numberInteger = 10
numberFloat = 20.1123
numberNegativ = -10
numbers = [10, 20, 30, 40, 50]

# print the type of the numbers
#
print(abs(numberNegativ))
print(round(numberFloat, 2))
print(int(numberFloat))
print(float(numberInteger))
print(complex(numberInteger, numberFloat))
print(pow(numberInteger, 2))
# return the division and the rest of the division
print(divmod(numberInteger, 3))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(bin(numberInteger))
print(oct(numberInteger))
print(hex(numberInteger))
print(bool(numberInteger))

# funtions maths Module ( import math )
# =====================

# math.sqrt() return the square root of a number

print(math.sqrt(numberInteger))
print(math.pow(numberInteger, 2))
print(math.exp(1))
# return the natural logarithm of a number
print(math.log(10))

# math.sin() return the sine of a number
# math.cos() return the cosine of a number
# math.tan() return the tangent of a number
# math.asin() return the arc sine of a number
# math.acos() return the arc cosine of a number
# math.atan() return the arc tangent of a number
# math.degrees() convert a number from radians to degrees
# math.ceil() return the smallest integer greater than or equal to a number
# math.floor() return the largest integer less than or equal to a number
# math.factorial() return the factorial of a number
# math.gcd() return the greatest common divisor of two numbers
# math.isclose() return True if two numbers are close to each other
#
#
# functions complex module ( import cmath )
# ========================
#

# cmath.phase() return the phase of a complex number
# cmath.polar() return the polar coordinates of a complex number
# cmath.rect() return the rectangular coordinates of a complex number
