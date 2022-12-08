data = []

def partOne():
    count = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if i == 0 or i == (len(data) - 1) or j == 0 or j == (len(data[i]) - 1):
                count += 1
                continue
            curr = int(data[i][j])
            above, below = [], []
            left = list(map(int, data[i][0:j]))
            right = list(map(int, data[i][j+1:len(data[i])]))
            for k in range(len(data)):
                if k < i:
                    above.append(int(data[k][j]))
                elif k > i:
                    below.append(int(data[k][j]))
                else:
                    continue

            if not any(w >= curr for w in above) or not any(x >= curr for x in below) or not any(y >= curr for y in left) or not any(z >= curr for z in right):
                count += 1      
    print(count)

def partTwo():
    top = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            sup, sdown, sleft, sright = 0, 0, 0, 0
            curr = int(data[i][j])
            above = []
            below = []
            left = list(map(int, data[i][0:j]))
            right = list(map(int, data[i][j+1:len(data[i])]))
            for k in range(len(data)):
                if k < i:
                    above.append(int(data[k][j]))
                elif k > i:
                    below.append(int(data[k][j]))
                else:
                    continue

            above.reverse()
            left.reverse()

            # There's definitely a cleaner way to do this
            for x in above:
                sup += 1
                if x >= curr:
                    break
            for x in below:
                sdown += 1
                if x >= curr:
                    break
            for x in left:
                sleft += 1
                if x >= curr:
                    break
            for x in right:
                sright += 1
                if x >= curr:
                    break
            top = max(top, (sup*sdown*sleft*sright))

    print(top)

if __name__ == "__main__":
    data = open("input08.txt", "r").read().splitlines()
    partOne()
    partTwo()