f = open("input_real.txt", "r")
a = f.read()

result = 0
for line in a.splitlines():
    dimensions = [int(x) for x in line.split('x')]
    dimensions.sort()
    result += (dimensions[0] * 2 + dimensions[1] * 2) + (dimensions[0] * dimensions[1] * dimensions[2])
print(result)
