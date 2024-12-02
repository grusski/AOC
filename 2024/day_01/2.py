f = open("input_real.txt", "r")
# f = open("input_test.txt", "r")
a = f.read()

first_numbers = []
second_numbers = []
for line in a.split('\n'):
    first_numbers.append(int(line.split('   ')[0]))
    second_numbers.append(int(line.split('   ')[1]))

answer = 0

for element in first_numbers:
    answer += element * second_numbers.count(element)

print(answer)