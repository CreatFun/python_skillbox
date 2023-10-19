def get_amount_of_letters(string):
    letters_and_amount = dict()
    for i in string:
        if letters_and_amount.get(i) is None:
            letters_and_amount[i] = 1
        else:
            letters_and_amount[i] += 1
    return letters_and_amount


file_name = input()
file = open(file_name + ".txt", "r", encoding="utf-8")
string_from_file = file.read()
file.close()

string_for_check = ""
for sym in string_from_file:
    if sym.isalpha():
        string_for_check += sym

dict_letters_amount = get_amount_of_letters(string_for_check)
sorted_list = sorted(dict_letters_amount.items(), key=lambda x: x[1])

result_file = open("result_task5.txt", "w", encoding="utf-8")
for i in sorted_list:
    result_file.write(f"{i[0]}: {i[1]} \n")
result_file.close()
