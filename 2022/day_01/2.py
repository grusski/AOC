f = open("input_real.txt", "r")
a = f.read()

a_split = a.split('\n')

superlist = list()
temp = []

for item in a_split:
    if item != '':
        temp.append(int(item))
    else:
        superlist.append(temp)

        temp = []
        continue

#print(superlist)
elves_calories = []
for item in superlist:
    elves_calories.append(sum(item))


print(sum(sorted(elves_calories, reverse=True)[:3]))
