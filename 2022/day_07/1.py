from anytree import Node, RenderTree

f = open("input_real.txt", "r")
a = f.read()

totalsum = 0

for line in a.splitlines():
    if line == '$ cd /':
        root = Node("/", dir=True)
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

#print(RenderTree(root))
#print("-----")

for directory in root.descendants:
    dir_size = 0
    if not directory.isDir:
        continue
    else:
        for node in directory.descendants:
            if not node.isDir:
                dir_size += node.size
        if dir_size <= 100000:
            totalsum += dir_size

print(totalsum)
