
f = open("input_real.txt", "r")
a = f.read()

sum = 0
c = 0
lines_temp = []

for line in a.splitlines():
    lines_temp.append(line)
    c += 1
    if c % 3 == 0:
        for char in lines_temp[0]:
            if(lines_temp[1].find(char)) != -1:
                if(lines_temp[2].find(char)) != -1:
                    if ord(char) <= 90:
                        sum += ord(char)-38
                    else:
                        sum += ord(char)-96

                    lines_temp = []
                    break
print(sum)
