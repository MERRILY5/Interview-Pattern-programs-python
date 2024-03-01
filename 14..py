 for i in range(5):
     for j in range(5):
         print(5 * j + (5 - i), end=" ")
     print()


##OR

 for i in range(5):
     for j in range(5):
         if i % 2 == 0:
             print((j+1)*5 - i, end=' ')
         else:
             print(j*5 + 5 - i, end=' ')
     print()
