decimal_num = int(input)

# binary
number = decimal_num
binary_num = ""
while number > 0:
    binary_num += str(number % 2)
    number //= 2

print(binary_num[::-1])

# octal
number = decimal_num
octal_num = ""
while number > 0:
    octal_num += str(number % 8)
    number //= 8

print(octal_num[::-1])

# hexadecimal
number = decimal_num
hexadecimal_num = ""
while number > 0:
    if (number % 16 == 10):
        hexadecimal_num += "A"
    elif (number % 16 == 11):
        hexadecimal_num += "B"
    elif (number % 16 == 12):
        hexadecimal_num += "C"
    elif (number % 16 == 13):
        hexadecimal_num += "D"
    elif (number % 16 == 14):
        hexadecimal_num += "E"
    elif (number % 16 == 15):
        hexadecimal_num += "F"
    else:
        hexadecimal_num += str(number % 16)
    number //= 16

print(hexadecimal_num[::-1])