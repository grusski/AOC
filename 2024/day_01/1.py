f = open("input_real.txt", "r")
# f = open("input_test.txt", "r")
a = f.read()

first_numbers = []
second_numbers = []
for line in a.split('\n'):
    first_numbers.append(int(line.split('   ')[0]))
    second_numbers.append(int(line.split('   ')[1]))

first_numbers.sort()
second_numbers.sort()

answer = 0

for (i, j) in zip(first_numbers, second_numbers):
    answer += abs(j - i)

print(answer)