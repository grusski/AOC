f = open("input_real.txt", "r")
a = f.read()

sum = 0

for line in a.splitlines():
    part1 = line[:len(line)//2]
    part2 = line[len(line)//2:]

    for char in part1:
        if(part2.find(char)) != -1:
            if ord(char) <= 90:
                sum += ord(char)-38
            else:
                sum += ord(char)-96
            break

print(sum)

