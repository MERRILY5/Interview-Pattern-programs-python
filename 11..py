for i in range(1,6):
    for j in range(1,7):
        if j%2==0:
            print((j//2),end=" ")
        else:
            print(i,end=" ")
    print()

##OR

for i in range(1,6):
    for j in range(1,4):
        print(i,j,end=" ")
    print()
