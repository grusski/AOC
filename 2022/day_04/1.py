f = open("input_real.txt", "r")
a = f.read()


counter = 0


for line in a.splitlines():

    part1 = line.split(',')[0]
    part2 = line.split(',')[1]

    part1_1 = int(part1.split('-')[0])
    part1_2 = int(part1.split('-')[1])

    part2_1 = int(part2.split('-')[0])
    part2_2 = int(part2.split('-')[1])

    if part2_1 <= part1_1 <= part2_2 and part2_1 <= part1_2 <= part2_2 or part1_1 <= part2_1 <= part1_2 and part1_1 <= part2_2 <= part1_2:
        counter += 1


print(counter)