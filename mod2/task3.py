string = input()
str_length = len(string)

a = -10000
b = -10000
c = -10000

number = ""

sym_count = 0
for symbol in string:
    if (symbol.isdigit()) or (symbol == "-"):
        number += symbol
    else:
        if (a < -1000):
            a = int(number)
        elif (b < -1000):
            b = int(number)
        number = ""
    
    sym_count += 1

    if (sym_count == str_length):
            c = int(number)    

mid_number = (a + b + c) - max(a, b, c) - min(a, b, c)
print(mid_number) 

