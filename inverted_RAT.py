r = 5
c = 5

for row in range(1, r+1):
    for col in range(r-row+1):
        print("*", end=" ")

    print()    