f = open("input_real.txt", "r")
a = f.read()

print(a.count('(') - a.count(')'))
