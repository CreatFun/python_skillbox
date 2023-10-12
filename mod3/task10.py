size = int(input())
matrix_1 = [[x for x in range(1, size + 1)] for y in range(1, size + 1)]

for i in matrix_1:
    print(i)

print()

transposed_matrix = list()
for i in range(len(matrix_1[0])):
    row = list()
    for sublist in matrix_1:
        row.append(sublist[i])
    transposed_matrix.append(row)

for i in transposed_matrix:
    print(i)
