f = open("input_real.txt", "r")
a = f.read()

stacks = a[0:a.find('1')-2]
numberOfStacks = int(a[a.find('1'):a.find('move')-2].split(' ')[-2:-1][0])
moves = a[a.find('move'):]

stacks_cleaned = stacks.replace('    ', '0')
stacks_cleaned = stacks_cleaned.replace('[', '')
stacks_cleaned = stacks_cleaned.replace(']', '')
stacks_cleaned = stacks_cleaned.replace(' ', '')

superstack = []

for x in range(numberOfStacks):
    stack_temp = []
    for y in range(x, len(stacks_cleaned), numberOfStacks+1):
        if stacks_cleaned[y] == '0':
            continue
        else:
            stack_temp.append(stacks_cleaned[y])
    superstack.append(stack_temp)

for item in superstack:
    item.reverse()


for line in moves.splitlines():
    order = line.split(' ')     # ['move', '1', 'from', '2', 'to', '1']
    list_temp = []
    for item in range(int(order[1])):
        list_temp.append(superstack[int(order[3])-1].pop())
    for item in reversed(list_temp):
        superstack[int(order[5])-1].append(item)


for item in superstack:
    print(item[-1:][0],end='')