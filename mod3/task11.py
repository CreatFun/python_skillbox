a = input()
size = len(a)

some_list = list()
some_list.append(a)


for i in range(size-1):
    some_list.append(input())

result = "Ничья"
isResultKnown = False

# Проверяем ряды
for string in some_list:
    if string.count("X") == size:
        result = "X"
        isResultKnown = True
        break
    elif string.count("O") == size:
        result = "O"
        isResultKnown = True
        break

# Проверяем столбцы
if not isResultKnown:
    string = ""
    for i in range(size):
        for j in range(size):
            string += some_list[j][i]
        if string.count("X") == size:
            result = "X"
            isResultKnown = True
            break
        elif string.count("O") == size:
            result = "O"
            isResultKnown = True
            break
        string = ""

# Проверяем первую диагональ
if not isResultKnown:
    # checking_index = 0
    string = ""
    for i in range(size):
        string += some_list[i][i]
        # checking_index += 1
    if string.count("X") == size:
        result = "X"
        isResultKnown = True
    elif string.count("O") == size:
        result = "O"
        isResultKnown = True

# Проверяем вторую диагональ
if not isResultKnown:
    checking_index = size - 1
    string = ""
    for i in range(size):
        string += some_list[i][checking_index]
        checking_index -= 1
    if string.count("X") == size:
        result = "X"
    elif string.count("O") == size:
        result = "O"

print(result)



