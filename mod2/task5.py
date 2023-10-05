string = input()



symbol = string[0]

number = ""
for i in string:
    if (i.isdigit() or i == "-"):
        number += i

step = int(number)

sym_code = ord(symbol)


flag = True
new_sym_code = sym_code
step_count = 0
while True:
    if step_count == step:
        break

    if (new_sym_code >= 97) and (new_sym_code <= 122):
        if (step > 0):
            new_sym_code += 1 
            step_count += 1
        else:
            new_sym_code -= 1
            step_count -= 1
    if (new_sym_code > 122):
        new_sym_code -= 26
    if (new_sym_code < 97):
        new_sym_code += 26

print(chr(new_sym_code))


