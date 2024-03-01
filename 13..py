for i in range(1,6):
    for j in range(0,5):
        if j==3:
            print(((22-i)-1),end=" ")
        elif j%2!=0:
          print(((12-i)-1),end=" ")
        else:
            print(i+j*5,end=" ")
    print()
