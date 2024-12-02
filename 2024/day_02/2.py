def check_difference(val_1, val_2):
    return abs(int(val_2) - int(val_1))


def check_conditions(row):
    for index, value in enumerate(row):
        if index == 0:
            continue
        elif index == 1:
            if check_difference(row[index - 1], value) > 3:
                direction = 'difference_too_big'
                break
            elif check_difference(row[index - 1], value) == 0:
                direction = 'equal'
                break
            if row[index - 1] < value:
                direction = 'up'
            elif row[index - 1] > value:
                direction = 'down'
        else:
            if direction == 'down':
                if check_difference(row[index - 1], value) > 3:
                    direction = 'difference_too_big'
                    break
                elif check_difference(row[index - 1], value) == 0:
                    direction = 'equal'
                    break
                elif row[index - 1] > value:
                    direction = 'down'
                else:
                    direction = 'not_one_direction'
                    break
            if direction == 'up':
                if check_difference(row[index - 1], value) > 3:
                    direction = 'difference_too_big'
                    break
                elif check_difference(row[index - 1], value) == 0:
                    direction = 'equal'
                    break
                elif row[index - 1] < value:
                    direction = 'up'
                else:
                    direction = 'not_one_direction'
                    break

    if direction == 'up' or direction == 'down':
        return 1
    else:
        return 0


f = open("input_real.txt", "r")
# f = open("input_test.txt", "r")
a = f.read()

answer = 0

for line in a.split('\n'):
    row = line.split(' ')
    for i in range(len(row)):
        row[i] = int(row[i])

    for i in range(len(row)):
        temp = row.copy()
        if i == 0 and check_conditions(temp) == 1:
            answer += 1
            break
        else:
            temp.pop(i)
            if 1 == check_conditions(temp):
                answer += 1
                break

print(answer)
