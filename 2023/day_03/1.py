

from string import punctuation




def find_all_neighbours(pos):
    neigbours = []
    neigbours.append([pos[0], pos[1] + 1])
    neigbours.append([pos[0], pos[1] - 1])
    neigbours.append([pos[0] + 1, pos[1]])
    neigbours.append([pos[0] - 1, pos[1]])
    # diags
    neigbours.append([pos[0] - 1, pos[1] + 1])
    neigbours.append([pos[0] + 1, pos[1] + 1])
    neigbours.append([pos[0] - 1, pos[1] - 1])
    neigbours.append([pos[0] + 1, pos[1] - 1])
    return neigbours


def check_neighbours(pos):
    neighbours = find_all_neighbours(pos)
    for n in neighbours:
        for s in system:
            if s[0] == n:
                if s[1] in punctuation:
                    return False

    return True



def neighbours_adjacent(positions):
    for x in positions:
        # print(x)
        check_neighbours(x)
    # print()

    # print(positions)
    # print(positions[1])

    for x, line in enumerate(a_split):
        for y, c in enumerate(line):
            # print(x, y)
            pass


f = open("input_test.txt", "r")
a = f.read()

a_split = a.split('\n')

number_temp = ''
number_temp_pos = []

number_temp_combined = ()

list_numbers = []

system = []

for x, line in enumerate(a_split):
    for y, c in enumerate(line):
        system.append(([x, y], c))
        if c.isdigit():
            number_temp += c
            number_temp_pos.append([x, y])

        else:
            if number_temp != '':
                number_temp_combined = (number_temp, number_temp_pos)
                list_numbers.append(number_temp_combined)

            # list_numbers.append(number_temp)
            # list_numbers_pos.append(number_temp_pos)
            number_temp = ''
            number_temp_pos = []

# print(list_numbers)


for item in list_numbers:
    neighbours_adjacent(item[1])
