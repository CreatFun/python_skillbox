string = input()


count_0 = 0
count_1 = 0

for i in string:
    if (i == "0"):
        count_0 += 1
    else:
        count_1 += 1

if (count_1 == count_0):
    print("yes")
else:
    print("no")

        



