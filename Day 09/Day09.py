data = []

def checkAdj(h, t):
    adj = False
    if t == (h[0], h[1] + 1): adj = True
    elif t == (h[0], h[1] - 1): adj = True
    elif t == (h[0] + 1, h[1]): adj = True
    elif t == (h[0] - 1, h[1]): adj = True
    elif t == (h[0] + 1, h[1] + 1): adj = True
    elif t == (h[0] - 1, h[1] + 1): adj = True
    elif t == (h[0] + 1, h[1] - 1): adj = True
    elif t == (h[0] - 1, h[1] - 1): adj = True
    elif t == (h[0], h[1]): adj = True
    return adj

def reposition(pos):
    temp = pos
    for i in range(1, len(temp)):
        hpos = temp[i-1]
        tpos = temp[i]

        while not checkAdj(hpos, tpos):
            disp = (hpos[0] - tpos[0], hpos[1] - tpos[1])
            disp = (hpos[0] - tpos[0], hpos[1] - tpos[1])   
            if not (disp[0]) * (disp[1]) == 0:
                if (disp[0] > 0) and (disp[1] > 0): tpos = (tpos[0] + 1, tpos[1] + 1)
                elif (disp[0] < 0) and (disp[1] > 0): tpos = (tpos[0] - 1, tpos[1] + 1)
                elif (disp[0] < 0) and (disp[1] < 0): tpos = (tpos[0] - 1, tpos[1] - 1)
                elif (disp[0] > 0) and (disp[1] < 0): tpos = (tpos[0] + 1, tpos[1] - 1)
            else:
                if disp[0] > 0: tpos = (tpos[0] + 1, tpos[1])
                elif disp[0] < 0: tpos = (tpos[0] - 1, tpos[1])
                elif disp[1] > 0: tpos = (tpos[0], tpos[1] + 1)
                elif disp[1] < 0: tpos = (tpos[0], tpos[1] - 1)
        
        temp[i-1] = hpos
        temp[i] = tpos
    return temp

def partOne():
    covered = []
    pos = [(0,0),(0,0)]
    covered.append(pos[1])
    for x, i in enumerate(data):
        command = i.split()
        for j in range(int(command[1])):
            match command[0]:
                case "U": pos[0] = (pos[0][0], pos[0][1] + 1)
                case "D": pos[0] = (pos[0][0], pos[0][1] - 1)
                case "L": pos[0] = (pos[0][0] - 1), pos[0][1]
                case "R": pos[0] = (pos[0][0] + 1), pos[0][1]
            pos = reposition(pos)
            covered.append(pos[1])
    print(len(set(covered)))

def partTwo():
    covered = []
    pos = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    covered.append(pos[9])
    for x, i in enumerate(data):
        command = i.split()
        for j in range(int(command[1])):
            match command[0]:
                case "U": pos[0] = (pos[0][0], pos[0][1] + 1)
                case "D": pos[0] = (pos[0][0], pos[0][1] - 1)
                case "L": pos[0] = (pos[0][0] - 1), pos[0][1]
                case "R": pos[0] = (pos[0][0] + 1), pos[0][1]
            pos = reposition(pos)
            covered.append(pos[9])
    print(len(set(covered)))

if __name__ == "__main__":
    data = open("input09.txt", "r").read().splitlines()
    partOne()
    partTwo()