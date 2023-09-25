import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for i in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# For transpose matrix and make a list out of it
matrix = list(zip(*matrix))

# for converting list in to string
new_string = str()

for i in matrix:
    for j in i:
        new_string = new_string + j

# for replacing  special character or double space between alphanumeric character to a single space

print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', new_string))
