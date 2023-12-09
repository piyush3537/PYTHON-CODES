#function which take 2 number as input and returns their sum
def add(n1=5,n2=6):
    print("n1:",n1)
    print("n2:",n2)
    sum=n1+n2
    return sum
#positional arguements
print("the sum ",add(3,2))

#keyword arguement(named arguements)
print("the sum is",add(n2=2,n1=3))

#default arguements
print("the sum is ",add(6))