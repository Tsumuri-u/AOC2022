data = []

def partOne():
    overlappers = 0
    for i in data:
        first = i.split(",")[0]
        second = i.split(",")[1]
        oneStart = int(first.split("-")[0])
        oneEnd = int(first.split("-")[1])
        twoStart = int(second.split("-")[0])
        twoEnd = int(second.split("-")[1])

        if ((oneStart <= twoStart and oneEnd >= twoEnd) or (twoStart <= oneStart and twoEnd >= oneEnd)):
            overlappers += 1

    print(overlappers)

def partTwo():
    overlappers = 0
    for i in data:
        first = i.split(",")[0]
        second = i.split(",")[1]
        oneStart = int(first.split("-")[0])
        oneEnd = int(first.split("-")[1])
        twoStart = int(second.split("-")[0])
        twoEnd = int(second.split("-")[1])

        if ((twoStart <= oneStart <= twoEnd) or (twoStart <= oneEnd <= twoEnd) or (oneStart <= twoStart <= oneEnd) or oneStart <= twoEnd <= oneEnd):
            overlappers += 1

    print(overlappers)



if __name__ == "__main__":
    with open('input04.txt') as f:
        data = [line.rstrip() for line in f]
    partOne()
    partTwo()