f = open("input_real.txt", "r")
a = f.read()

santa_houses_visited = []
robo_houses_visited = []

santa_current_position = [0, 0]
robo_current_position = [0, 0]

santa_houses_visited.append(santa_current_position[:])
robo_houses_visited.append(robo_current_position[:])

turn = 0

for char in a:
    # print(char)
    if turn % 2 == 0:
        match char:
            case ('>'):
                santa_current_position[0] = santa_current_position[0] + 1
                santa_houses_visited.append(santa_current_position[:])
            # print('right')
            case ('v'):
                santa_current_position[1] = santa_current_position[1] - 1
                santa_houses_visited.append(santa_current_position[:])
                # print('down')
            case ('<'):
                santa_current_position[0] = santa_current_position[0] - 1
                santa_houses_visited.append(santa_current_position[:])
                # print('left')
            case ('^'):
                santa_current_position[1] = santa_current_position[1] + 1
                santa_houses_visited.append(santa_current_position[:])
                # print('up')
    else:
        match char:
            case ('>'):
                robo_current_position[0] = robo_current_position[0] + 1
                robo_houses_visited.append(robo_current_position[:])
                # print('right')
            case ('v'):
                robo_current_position[1] = robo_current_position[1] - 1
                robo_houses_visited.append(robo_current_position[:])
                # print('down')
            case ('<'):
                robo_current_position[0] = robo_current_position[0] - 1
                robo_houses_visited.append(robo_current_position[:])
                # print('left')
            case ('^'):
                robo_current_position[1] = robo_current_position[1] + 1
                robo_houses_visited.append(robo_current_position[:])
                # print('up')
    turn += 1

merged_list = santa_houses_visited + robo_houses_visited

deduplicated_houses_visited = []
for item in merged_list:
    if item not in deduplicated_houses_visited:
        deduplicated_houses_visited.append(item)

print(len(deduplicated_houses_visited))
