import re

answer = 0

# f = open("input_test_2.txt", "r")
f = open("input_real_2.txt", "r")
a = f.read()

muls = re.findall("(mul\(\d*,\d*\)|don't\(\)|do\(\))", a)

skip = False

for mul in muls:
    if mul == "don't()":
        skip = True
        continue
    if mul == "do()":
        skip = False
        continue
    if not skip:
        answer += int(mul[4:-1].split(',')[0]) * int(mul[4:-1].split(',')[1])

print(answer)
