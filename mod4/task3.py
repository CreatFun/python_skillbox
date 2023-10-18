def find_greatest_common_divisor(num1, num2):
    if num1 == 0:
        return num2
    return find_greatest_common_divisor(num2 % num1, num1)


num1 = int(input())
num2 = int(input())
print(find_greatest_common_divisor(num1, num2))