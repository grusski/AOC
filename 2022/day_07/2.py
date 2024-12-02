from anytree import Node, RenderTree, PreOrderIter

f = open("input_real.txt", "r")
a = f.read()

totalsum = 0
nodes = []

for line in a.splitlines():
    if line == '$ cd /':
        root = Node("/", isDir=True)
        currentParent = root
    elif line == '$ ls':
        continue
    elif line != '$ cd ..' and line.split(' ')[0] == '$' and line.split(' ')[1] == 'cd':
        for child in currentParent.children:
            if child.name == line.split(' ')[2]:
                currentParent = child
    elif line == '$ cd ..':
        currentParent = currentParent.parent
    elif line.split(' ')[0] == 'dir':
        Node(line.split(' ')[1], parent=currentParent, isDir=True)
    elif line.split(' ')[0] != '$' and line.split(' ')[0] != 'dir':
        Node(line.split(' ')[1], parent=currentParent, isDir=False, size=int(line.split(' ')[0]))

for directory in PreOrderIter(root):
    dir_size = 0
    if not directory.isDir:
        continue
    else:
        for node in directory.descendants:
            if not node.isDir:
                dir_size += node.size
        if dir_size <= 100000:
            totalsum += dir_size
    directory.size = dir_size


for node in PreOrderIter(root):
    if node.isDir:
        nodes.append([node.name, node.size])

nodes.sort(key = lambda x: x[1])

total_space = 70000000
used_space = nodes[-1:][0][1]
free_space = total_space - used_space
required_space = 30000000

for item in nodes:
    if (free_space + item[1]) >= required_space:
        print(item)
        break
