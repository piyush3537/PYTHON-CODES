'''def power(a,b):
    return a**b


##main code
num=int(input("enter"))
pw=int(input("enter"))
re=power(num,pw)
print(f'power of a number{num} raised to {pw} is {re}')'''

def power(a,b):
    s=1
   for i in range(b):
        s*=a
   return s


##main code
num=3
pw=5
re  = power(num,pw)
print(f'power of a number{num} raised to {pw} is {re}')