f = open("input_real.txt", "r")
a = f.read()


counter = 4

for x in range(len(a)):
    found_duplicate = False
    temp = a[x:x+4]
    for item in temp:
        if temp.count(item) > 1:
            found_duplicate = True
            break
    if not found_duplicate:
        print(temp)
        print(counter)
        break
    counter += 1
