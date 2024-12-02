def find_first_cipher(input):
    for character in input:
        if character.isnumeric():
            return character


def find_last_cipher(input):
    for character in reversed(input):
        if character.isnumeric():
            return character


f = open("input_real.txt", "r")
a = f.read()

a_split = a.split('\n')

number_temp = 0

for line in a_split:
    number_temp += int((find_first_cipher(line) + find_last_cipher(line)))

print(number_temp)
