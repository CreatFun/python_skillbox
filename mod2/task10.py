string = input()

new_word = ""

for i in range(0, len(string)):
    if (string[i] == " "):
        new_word += string[i - 1]
    elif (i == len(string) - 1):
        new_word += string[i]

print(new_word)
