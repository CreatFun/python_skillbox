string = input()


vowels = "ёуеыаоэяию"
consonants = "йцкнгшщзхфвпрлджчсмтб"

vowels_count = 0
consonants_count = 0

for i in string:
    if i in vowels:
        vowels_count += 1
    elif i in consonants:
        consonants_count += 1

print(vowels_count, consonants_count)




        



