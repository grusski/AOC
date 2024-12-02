f = open("input_real.txt", "r")
a = f.read()

houses_visited = []
current_position = [0, 0]
houses_visited.append(current_position[:])

for char in a:
    # print(char)
    match char:
        case ('>'):
            current_position[0] = current_position[0] + 1
            houses_visited.append(current_position[:])
            # print('right')
        case ('v'):
            current_position[1] = current_position[1] - 1
            houses_visited.append(current_position[:])
            # print('down')
        case ('<'):
            current_position[0] = current_position[0] - 1
            houses_visited.append(current_position[:])
            # print('left')
        case ('^'):
            current_position[1] = current_position[1] + 1
            houses_visited.append(current_position[:])
            # print('up')

print(houses_visited)
print(len(houses_visited))
print('------------')

deduplicated_houses_visited = []
for item in houses_visited:
    if item not in deduplicated_houses_visited:
        deduplicated_houses_visited.append(item)
        
print(deduplicated_houses_visited)
print(len(deduplicated_houses_visited))
print('------------')