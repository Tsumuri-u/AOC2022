data = []

def partOne():
    sum = 0
    dupes = []

    for i in data:
        common = list(set(i[0:len(i)//2]) & set(i[len(i)//2:len(i)]))
        dupes.extend(common)
            
    for d in dupes:
        if (ord(d) < 91):
            sum += ord(d) - 38
        else:
            sum += ord(d) - 96

    print(sum)

def partTwo():
    sum = 0
    dupes = []

    for i in range(0, len(data), 3):
        common = list(set(data[i]) & set(data[i+1]) & set(data[i+2]))
        dupes.extend(common)
    
    for d in dupes:
        if (ord(d) < 91):
            sum += ord(d) - 38
        else:
            sum += ord(d) - 96

    print(sum)

if __name__ == "__main__":
    with open('input03.txt') as f:
        data = [line.rstrip() for line in f]
    partOne()
    partTwo()