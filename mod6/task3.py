def armstrong_numbers_generator():
    num = 10
    while True:
        digits = [int(digit) for digit in str(num)]  # коллекция из цифр числа
        digits_count = len(digits)  # количество цифр в числе
        sum_of_powers = sum([digit ** digits_count for digit in digits])  # сумма цифр возведенных в степень = кол-ву цифр
        if sum_of_powers == num:
            yield num
        num += 1


generator = armstrong_numbers_generator()


def get_armstrong_numbers():
    return next(generator)


for i in range(8):
    print(get_armstrong_numbers(), end=" ")

# Ожидаемый результат кода:
# 153 370 371 407 1634 8208 9474 54748
