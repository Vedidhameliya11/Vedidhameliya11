for i in range(1,8):
    for j in range(1, i+1):
        print(j, end="")
    print()

for i in range(7,0,-1):
    for j in range(1, i+1):
        print(j, end="")
    print()

n = 7

for i in range(0,7):
    for j in range(0, i+1):
        print("*", end="")
    print("")

for i in range(7,0,-1):
    for j in range(0, i+0):
        print("*", end="")
    print("")

number = 1
stop = 1
rows = 7

for i in range(rows):
    for j in range(1, stop):
        print(number, end="")
        number+=1
    print("")
    stop+=1

rows = 6

for i in range(7):
    for j in range(i):
        print(i, end="")
    print("")