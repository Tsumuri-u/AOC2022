tree = {'dirs': {}, 'files': {}, 'parent': None}
remove = 100000000

def buildTree():
    root = tree
    for i in open("input07.txt", "r").readlines():
        command = i.split()
        if (command == ['$', 'cd', '/']):
            continue
        elif (command == ['$', 'ls']):
            continue
        elif (command == ['$', 'cd', '..']):
            root = root['parent']
        elif (command[0] == '$' and command[1] == 'cd'):
            root = root['dirs'][command[2]]
        elif (command[0] == 'dir'):
            root['dirs'][command[1]] = {'dirs': {}, 'files': {}, 'parent': root}
        else:
            root['files'][command[1]] = int(command[0])

def computeSize(root):
    sum = 0
    for i in root['dirs'].values():
        computeSize(i)
        sum += i['size']
    for j in root['files'].values():
        sum += j
    root['size'] = sum

def partOne(root):
    sum = 0
    for i in root['dirs'].values():
        sum += partOne(i)
    if (root['size'] < 100000):
        sum += root['size']
    return sum

def partTwo(root):
    global remove
    for i in root['dirs'].values():
        partTwo(i)
    if (root['size'] > 30000000 - (70000000 - tree['size'])):
        remove = min(root['size'], remove)
    return remove
    
if __name__ == "__main__":
    buildTree()
    computeSize(tree)
    print(partOne(tree))
    print(partTwo(tree))