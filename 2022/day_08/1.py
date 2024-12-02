from anytree import Node, RenderTree

result = 0


def check_if_visible(row, column):
    global result

    for i in range(row - 1, -1, -1):
        if matrix[i][column] < matrix[row][column]:
            if i == 0:
                result = result + 1
                return
            else:
                continue
        else:
            break

    for i in range(row + 1, matrix_len, 1):
        if matrix[i][column] < matrix[row][column]:
            if i == len(matrix[0]) - 1:
                result = result + 1
                return
            else:
                continue
        else:
            break

    for i in range(column + 1, matrix_len, 1):
        if matrix[row][i] < matrix[row][column]:
            if i == len(matrix[0]) - 1:
                result = result + 1
                return
            else:
                continue
        else:
            break

    for i in range(column - 1, -1, -1):
        if matrix[row][i] < matrix[row][column]:
            if i == 0:
                result = result + 1
                return
            else:
                continue
        else:
            break


f = open("input_real.txt", "r")
a = f.read()

matrix = []

for line in a.splitlines():
    line_array = []
    for char in line:
        line_array.append(char)
    matrix.append(line_array)

matrix_len = len(matrix)

for row in range(1, len(matrix[0]) - 1):
    for column in range(1, len(matrix[0]) - 1):
        check_if_visible(row, column)

print(result + (matrix_len * 4 - 4))
