data = []

def partOne():
    checker = []
    count = 0

    for i in data:
        checker.append(i)
        count += 1

        if (len(checker) == 4):
            if (len(set(checker)) == 4):
                print('Count: ', count)
                break
            else:
                checker.pop(0)
        
def partTwo():
    checker = []
    count = 0

    for i in data:
        checker.append(i)
        count += 1

        if (len(checker) == 14):
            if (len(set(checker)) == 14):
                print('Count: ', count)
                break
            else:
                checker.pop(0)

if __name__ == "__main__":
    data = open("input06.txt", "r").read()
    partOne()
    partTwo()