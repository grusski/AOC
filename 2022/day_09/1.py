f = open("input_real.txt", "r")
a = f.read()

head_position = [0, 0]
tail_position = [0, 0]

head_positions = []
tail_positions = []
deduplicated_tail_positions = []


def is_in_sector():
    if tail_position[0] in range(head_position[0] - 1, head_position[0] + 2) and tail_position[1] in range(
            head_position[1] - 1, head_position[1] + 2):
        return True
    else:
        return False


def move_tail():
    # case head moves right
    if tail_position[1] in range(head_position[1] - 1, head_position[1] + 2) and tail_position[0] == head_position[
        0] - 2:
        tail_position[0] = head_position[0] - 1
        tail_position[1] = head_position[1]

    # case head moves left
    if tail_position[1] in range(head_position[1] - 1, head_position[1] + 2) and tail_position[0] == head_position[
        0] + 2:
        tail_position[0] = head_position[0] + 1
        tail_position[1] = head_position[1]

    # case head moves up
    if tail_position[0] in range(head_position[0] - 1, head_position[0] + 2) and tail_position[1] == head_position[
        1] - 2:
        tail_position[0] = head_position[0]
        tail_position[1] = head_position[1] - 1

    # case head moves down
    if tail_position[0] in range(head_position[0] - 1, head_position[0] + 2) and tail_position[1] == head_position[
        1] + 2:
        tail_position[0] = head_position[0]
        tail_position[1] = head_position[1] + 1


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
        tail_positions.append(tail_position[:])
        head_positions.append(head_position[:])


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
