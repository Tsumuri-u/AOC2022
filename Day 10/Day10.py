data = []

def partOne():
    bigsig = []
    clock, x, sum = 1, 1, 0
    for i in data:
        command = i.split()
        clock += 1
        if command[0] == 'addx':
            if clock == 20 or (clock - 20) % 40 == 0: bigsig.append(x)
            clock += 1
            x += int(command[1])
        
        if clock == 20 or (clock - 20) % 40 == 0: bigsig.append(x)

    for ind, i in enumerate(bigsig):
        if ind == 0: sum += i*20
        else: sum += i*(20 + (ind*40))
    print(sum)

def partTwo():
    clock, sprite = 1, (0,1,2)
    crt = []
    for i in data:
        command = i.split()
        ray = 40 if clock%40 == 0 else clock%40
        if ray in sprite: 
            crt.append('#')
        else: 
            crt.append('.')
        clock += 1
        if command[0] == 'addx':
            sprite = tuple(x + int(command[1]) for x in sprite)
            ray = 40 if clock%40 == 0 else clock%40
            if ray in sprite: 
                crt.append('#')
            else: 
                crt.append('.')
            clock += 1

    for i in range(len(crt)):
        print(crt[i], end='')
        if (i+1) % 40 == 0:
            print(" ")

if __name__ == "__main__":
    data = open("input10.txt", "r").read().splitlines()
    partOne()
    partTwo()