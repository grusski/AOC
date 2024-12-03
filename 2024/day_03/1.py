import re

answer = 0

# f = open("input_test_1.txt", "r")
f = open("input_real_1.txt", "r")
a = f.read()

muls = re.findall("mul\(\d*,\d*\)", a)

for mul in muls:
    answer += int(mul[4:-1].split(',')[0]) * int(mul[4:-1].split(',')[1])

print(answer)
