f = open("input_real.txt", "r")
a = f.read()

score = 0

for line in a.splitlines():
    b = line.split((' '))
    if b[0] == 'A' and b[1] == 'X':
        score += 4
    elif b[0] == 'A' and b[1] == 'Y':
        score += 8
    elif b[0] == 'A' and b[1] == 'Z':
        score += 3
    elif b[0] == 'B' and b[1] == 'X':
        score += 1
    elif b[0] == 'B' and b[1] == 'Y':
        score += 5
    elif b[0] == 'B' and b[1] == 'Z':
        score += 9
    elif b[0] == 'C' and b[1] == 'X':
        score += 7
    elif b[0] == 'C' and b[1] == 'Y':
        score += 2
    elif b[0] == 'C' and b[1] == 'Z':
        score += 6

print(score)

"""
A rock
B paper
C scisors


X rock 1
Y paper 2
Z scisors 3


loss 0
draw 3
win 6
"""