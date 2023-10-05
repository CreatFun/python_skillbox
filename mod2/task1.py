string = input()


a = 0
b = 0

digits = "1234567890"

number = ""
for i in range(0, len(string)):
    if (string[i] in digits) or (string[i] == "-"):
        number += string[i]
    elif (string[i] == ","):
        a = int(number)
        number = ""
    elif (string[i] == " "):
        continue

    if (i == len(string)-1):
        b = int(number)
        
    
print(a % b)
