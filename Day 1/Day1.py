data = []
totalList = []

def setup():
    fileObject = open("input01.txt", "r")
    lines = fileObject.readlines()

    for line in lines:
        if line == "\n":
            data.append("empty")
        else:
            data.append(line.strip())

def partOne():
    tempSum = 0
    for i in data:
        if i != "empty":
            tempSum += int(i)
        else:
            totalList.append(tempSum)
            tempSum = 0

    print(max(totalList))

def partTwo():
    partTwoList = totalList

    one = max(partTwoList)
    partTwoList.remove(one)
    two = max(partTwoList)
    partTwoList.remove(two)
    three = max(partTwoList)
    
    print(one + two + three)

if __name__ == "__main__":
    setup()
    partOne()
    partTwo()

