f = open("input_real.txt", "r")
a = f.read()

counter = 0
for i, char in enumerate(a):
    if char == '(':
        counter += 1
    elif char == ')':
        counter -= 1
    if counter == -1:
        print(i + 1)
        break
