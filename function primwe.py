def prime(n):
   count=0
   for i in range(1,n+1):
   if n%i==0:
        count+=1
        if count==2:
            return"prime"
        else:
            return"not prime"

##main code
n=int(input("enter the number"))
out=prime(n)
print(out)