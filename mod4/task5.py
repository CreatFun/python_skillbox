def get_amount_of_letters(string):
    letters_and_amount = dict()
    for i in string:
        if letters_and_amount.get(i) is None:
            letters_and_amount[i] = 1
        else:
            letters_and_amount[i] += 1
    return letters_and_amount


string = input()

dict_letters_amount = get_amount_of_letters(string)
sorted_list = sorted(dict_letters_amount.items(), key=lambda x: x[1])

result_file = open("result_task5.txt", "w", encoding="utf-8")
for i in sorted_list:
    result_file.write(f"{i[0]}: {i[1]} \n")
result_file.close()
