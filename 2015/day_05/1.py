f = open("input_real.txt", "r")
a = f.read()

vowels = 'aeiou'
not_allowed = ['ab', 'cd', 'pq', 'xy']
counter = 0

for line in a.splitlines():
    candidate = False
    vowel_counter = 0
    for letter in vowels:
        if not line.count(letter) == 0:
            vowel_counter += line.count(letter)
    if vowel_counter >= 3:
        candidate = True
    else:
        continue
    candidate = False
    for letter in line:
        if letter + letter in line:
            candidate = True
    for item in not_allowed:
        if item in line:
            candidate = False
            continue
    if candidate:
        counter += 1
        print(line)
print(counter)
