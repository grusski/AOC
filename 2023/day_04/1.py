
f = open("input_real.txt", "r")
a = f.read()

a_split = a.split('\n')
result = 0
for a in a_split:
    score = 0
    winning_numbers = a.split('|')[0].split(': ')[1].strip().replace('  ', ' ').split(' ')
    numbers_I_have = a.split('|')[1].strip().replace('  ', ' ').split(' ')
    for number in winning_numbers:
        if number in numbers_I_have:
            if score == 0:
                score = 1
            else:
                score *= 2
    result += score
    print(winning_numbers)
    print(numbers_I_have)
    print()
print(result)