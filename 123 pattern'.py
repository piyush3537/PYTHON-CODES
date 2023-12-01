
n=int(input("enters the numbers"))
for i in range(1,n+1):#for loop rows
    #printing spaces
    print(" "*(n-i),end="")
    #printing digits
    for j in range(1,2*i):
        print(j,end="")
    print()