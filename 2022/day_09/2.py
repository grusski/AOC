f = open("input_test.txt", "r")
a = f.read()

head_position = [0, 0]
# tail_position = [0, 0]

list_tails = []


k1 = [0,0]
list_tails.append(k1)
k2 = [0,0]
list_tails.append(k2)
k3 = [0,0]
list_tails.append(k3)
k4 = [0,0]
list_tails.append(k4)
k5 = [0,0]
list_tails.append(k5)
k6 = [0,0]
list_tails.append(k6)
k7 = [0,0]
list_tails.append(k7)
k8 = [0,0]
list_tails.append(k8)
k9 = [0,0]
list_tails.append(k9)



head_positions = []
tail_positions = []
deduplicated_tail_positions = []


def is_in_sector():
    if list_tails[0] in range(head_position[0] - 1, head_position[0] + 2) and list_tails[1] in range(
            head_position[1] - 1, head_position[1] + 2):
        return True
    else:
        return False


def move_tail():
    for i in range(0, len(list_tails)):
        if i == 0:
            previous_knot = head_position[:]
        else:
            previous_knot = list_tails[i-1]

        current_knot = list_tails[i]

        # case head moves right
        if current_knot[1] in range(previous_knot[1] - 1, previous_knot[1] + 2) and current_knot[0] == previous_knot[
            0] - 2:
            current_knot[0] = previous_knot[0] - 1
            current_knot[1] = previous_knot[1]

        # case head moves left
        if current_knot[1] in range(previous_knot[1] - 1, previous_knot[1] + 2) and current_knot[0] == previous_knot[
            0] + 2:
            current_knot[0] = previous_knot[0] + 1
            current_knot[1] = previous_knot[1]

        # case head moves up
        if current_knot[0] in range(previous_knot[0] - 1, previous_knot[0] + 2) and current_knot[1] == previous_knot[
            1] - 2:
            current_knot[0] = previous_knot[0]
            current_knot[1] = previous_knot[1] - 1

        # case head moves down
        if current_knot[0] in range(previous_knot[0] - 1, previous_knot[0] + 2) and current_knot[1] == previous_knot[
            1] + 2:
            current_knot[0] = previous_knot[0]
            current_knot[1] = previous_knot[1] + 1


def move_head(direction):
    for step in range(steps):
        if direction == 'right':
            head_position[0] = head_position[0] + 1
            if not is_in_sector():
                move_tail()
        elif direction == 'left':
            head_position[0] = head_position[0] - 1
            if not is_in_sector():
                move_tail()
        elif direction == 'up':
            head_position[1] = head_position[1] + 1
            if not is_in_sector():
                move_tail()
        elif direction == 'down':
            head_position[1] = head_position[1] - 1
            if not is_in_sector():
                move_tail()
        tail_positions.append(k9[:])
        #head_positions.append(head_position[:])
        
        
        # print(head_position, end='')
        # for item in list_tails:
        #     print(item, end='')
        # print()
        for x in range(20):
            for y in range(20):
                if head_position[0]+10 == x and head_position[1]+10 == y:
                    print('H', end='')
                for i in range(0, len(list_tails)):
                    if list_tails[i][0]+10 == x and list_tails[i][1]+10 == y:
                        print(str(i+1), end='')
                else:
                    print('.', end='')
                    
            print()
        print('----------')


for line in a.splitlines():
    steps = int(line.split(' ')[1])
    if line.split(' ')[0] == 'R':
        move_head('right')
    elif line.split(' ')[0] == 'L':
        move_head('left')
    elif line.split(' ')[0] == 'U':
        move_head('up')
    elif line.split(' ')[0] == 'D':
        move_head('down')

for item in tail_positions:
    if item not in deduplicated_tail_positions:
        deduplicated_tail_positions.append(item)

print(len(deduplicated_tail_positions))
