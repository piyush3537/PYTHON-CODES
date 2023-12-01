#print the given pattern
n=int(input("enter the number"))
for i in range(n):#for rows
    for j in range(1,n+1):#loop for column
        print(j, end="")
    print()