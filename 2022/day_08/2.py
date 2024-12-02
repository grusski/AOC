from anytree import Node, RenderTree


def calculate_scenic_score(row, column):
    counter_up = 0
    counter_down = 0
    counter_right = 0
    counter_left = 0

    # up
    for i in range(row - 1, -1, -1):
        a = matrix[i][column]
        b = matrix[row][column]
        if matrix[i][column] >= matrix[row][column]:
            counter_up += 1
            break
        elif matrix[i][column] < matrix[row][column]:
            counter_up += 1

    # left
    for i in range(column - 1, -1, -1):
        g = matrix[row][i]
        h = matrix[row][column]
        if matrix[row][i] >= matrix[row][column]:
            counter_left += 1
            break
        elif matrix[row][i] < matrix[row][column]:
            counter_left += 1

    # right
    for i in range(column + 1, matrix_len, 1):
        e = matrix[row][i]
        f = matrix[row][column]
        if matrix[row][i] >= matrix[row][column]:
            counter_right += 1
            break
        elif matrix[row][i] < matrix[row][column]:
            counter_right += 1

    # down
    for i in range(row + 1, matrix_len, 1):
        c = matrix[i][column]
        d = matrix[row][column]
        if matrix[i][column] >= matrix[row][column]:
            counter_down += 1
            break
        elif matrix[i][column] < matrix[row][column]:
            counter_down += 1

    return(counter_up*counter_left*counter_right*counter_down)
    # return ("" + str(counter_up) + "" + str(counter_left) + "" + str(counter_down) + "" + str(counter_right))


f = open("input_real.txt", "r")
a = f.read()

matrix = []
highest_scenic_counter = 0

for line in a.splitlines():
    line_array = []
    for char in line:
        line_array.append(char)
    matrix.append(line_array)

matrix_len = len(matrix)

for row in range(1, len(matrix[0]) - 1):
    for column in range(1, len(matrix[0]) - 1):
        scenic_counter_temp = calculate_scenic_score(row, column)
        if scenic_counter_temp > highest_scenic_counter:
            highest_scenic_counter = scenic_counter_temp

print(highest_scenic_counter)
