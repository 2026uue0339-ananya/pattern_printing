n=8

for row in range(1, n):
    for space in range(2*(n-row)):
        print(" ",end=" ")

    for star in range(2*row-1):
        print(" * " , end=" ")

    print()   


for row in range(n, 0, -1):
    for space in range(2*(n-row)):
        print(" ",end=" ")

    for star in range(2*row-1):
        print(" * " , end=" ")

    print()      