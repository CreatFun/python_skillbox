string = input()


numbers = "0123456789"

has_duplicates = False

for i in numbers:
    if (string.count(i) > 1):
        has_duplicates = True
        break

print(has_duplicates)
