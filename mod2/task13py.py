#string = input()

string = "4604075024433"

even_sum = 0
uneven_sum = 0

#even
for i in range(1, len(string), 2):
    even_sum += int(string[i])
    

#uneven
for i in range(0, len(string), 2):
    uneven_sum += int(string[i])
    
if ((uneven_sum + 3 * even_sum) % 10 == 0):
    print("yes")
else:
    print("no")



