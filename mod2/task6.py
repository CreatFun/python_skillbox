string = input()


dot_index = 0
output = ""


for i in range(len(string)-1, -1, -1):
    if (string[i] != "."):
        output = string[i] + output
    else:
        print(output)
        output = ""
    
    if (i == 0):
        print(output)

        



