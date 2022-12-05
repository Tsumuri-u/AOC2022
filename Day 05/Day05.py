data = []
stacks = [[],[],[],[],[],[],[],[],[]]

def buildStacks():
    temp = [[],[],[],[],[],[],[],[],[]]
    for i in range(8):
        for j in range(0, 35, 4):
            temp[j//4].append(data[i][j+1])
    
    for i in range(9):
        stacks[i].clear()
        for j in range(8):
            if (temp[i][j] != ' '):
                stacks[i].append(temp[i][j])

    for i in range(9):
        stacks[i].reverse()

def partOne():
    buildStacks()
    for i in range(10, len(data), 1):
        count = int(data[i].split(" ")[1])
        start = int(data[i].split(" ")[3]) - 1
        end = int(data[i].split(" ")[5]) - 1

        for j in range(count):
            stacks[end].append(stacks[start].pop())

    out = ""
    for i in range(9):
        out += stacks[i].pop()

    print(out)

def partTwo():
    buildStacks()
    for i in range(10, len(data), 1):
        count = int(data[i].split(" ")[1])
        start = int(data[i].split(" ")[3]) - 1
        end = int(data[i].split(" ")[5]) - 1

        temp = []
        for j in range(count):
            temp.append(stacks[start].pop())
        
        temp.reverse()
        stacks[end].extend(temp)

    out = ""
    for i in range(9):
        out += stacks[i].pop()

    print(out)


if __name__ == "__main__":
    with open('input05.txt') as f:
        data = [line.rstrip() for line in f]
    partOne()
    partTwo()