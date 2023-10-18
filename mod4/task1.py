def is_equal(list_for_check):
    is_equal_flag = True
    if len(list_for_check) > 1:
        for i in range(1, len(list_for_check)):
            if list_for_check[i] != list_for_check[i - 1]:
                is_equal_flag = False
                break

    return is_equal_flag


def is_different(list_for_check):
    if len(list_for_check) == len(set(list_for_check)):
        return True
    else:
        return False


input_list = input().split()


if len(input_list) == 0:
    print("Пустой")
elif is_equal(input_list):
    print("Все числа равны")
elif is_different(input_list):
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")