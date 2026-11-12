n= 10

for row in range(1, n+1):
    for col in range(row):
        if (col+row) %2 != 0 :
            print("1", end=" ")

        else:
            print("0",end=" ")  

    print()        