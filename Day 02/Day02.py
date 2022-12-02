data = []
opponentPlay = []
myPlay = []

def setup():
    fileObject = open("input02.txt", "r")
    lines = fileObject.read()
    count = 0

    for i in lines:
        if (count % 4 == 0):
            opponentPlay.append(i)
        elif (count % 4 == 2):
            myPlay.append(i)
        count += 1
    
def partOne():
    score = 0
    for i in range(len(opponentPlay)):
        if (opponentPlay[i] == 'A'):
            if (myPlay[i] == 'X'):
                score += 4
            elif (myPlay[i] == 'Y'):
                score += 8
            else:
                score += 3
        elif (opponentPlay[i] == 'B'):
            if (myPlay[i] == 'X'):
                score += 1
            elif (myPlay[i] == 'Y'):
                score += 5
            else:
                score += 9
        else:
            if (myPlay[i] == 'X'):
                score += 7
            elif (myPlay[i] == 'Y'):
                score += 2
            else:
                score += 6
    print(score)


def partTwo():
    score = 0
    for i in range(len(opponentPlay)):
        if (opponentPlay[i] == 'A'):
            if (myPlay[i] == 'X'):
                score += 3
            elif (myPlay[i] == 'Y'):
                score += 4
            else:
                score += 8
        elif (opponentPlay[i] == 'B'):
            if (myPlay[i] == 'X'):
                score += 1
            elif (myPlay[i] == 'Y'):
                score += 5
            else:
                score += 9
        else:
            if (myPlay[i] == 'X'):
                score += 2
            elif (myPlay[i] == 'Y'):
                score += 6
            else:
                score += 7
    print(score)
if __name__ == "__main__":
    setup()
    partOne()
    partTwo()
