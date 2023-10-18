def get_amount_of_letters(string):
    letters_and_amount = dict()
    for i in string:
        if letters_and_amount.get(i) is None:
            letters_and_amount[i] = 1
        else:
            letters_and_amount[i] += 1
    return letters_and_amount

def can_make_palindrome(letters_and_amount):
    n = len(letters_and_amount)
    e = 0
    for i in letters_and_amount.values():
        if i % 2 == 0:
            e += 1
    return e == n or e == n-1



def make_palindrome(letters_and_amount):
    odd_letters = ""
    for i in letters_and_amount:
        if letters_and_amount[i] % 2 != 0:
            odd_letters = i * letters_and_amount[i]
            del(letters_and_amount[i])
            break

    palindrome = odd_letters
    for i in letters_and_amount:
        palindrome = ((i * (letters_and_amount[i] // 2))
                      + palindrome
                      + (i * (letters_and_amount[i] // 2)))

    return palindrome


string = input()
letters_and_amount = get_amount_of_letters(string)

if can_make_palindrome(letters_and_amount):
    print(make_palindrome(letters_and_amount))
else:
    print("Невозможно составить палиндром")

