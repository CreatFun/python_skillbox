string = input()

counting_symbol = string[-1]
string_for_check = ""
for i in string:
    if (i != ","):
        string_for_check += i
    else:
        break


sym_count = 0
for i in string_for_check:
    if (i == counting_symbol):
        sym_count += 1
    else:
        break

print(sym_count)



        



