n=8

print(" * "*n)

for row in range(2,n):
    print(" * ", end=" ")
    for col in range(1,n-1):
        print("  ", end=" ")

    print("* ", end=" ") 
    print()   


print(" * "* n)