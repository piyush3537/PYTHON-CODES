'''def piyush(p,r,t):
    si=(p*r*t)/100
    print(si)

p=1000
r=3
t=5
piyush(p,r,t)


a=18980
b=2
c=7
piyush(a,b,c)'''

'''def greater(a,b):
 if (a>b):
  print("a is greater thsn b")
 else:
  print("b is greater")

a=4
b=9
greater(a,b)

n=8989
m=989
greater(n,m)'''

def is_lesser(j,k):
    pass



'''def average(a,b):
    print("the average of",(a+b)/2)

average(4,6)'''

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
   # print("average is:",sum/len(numbers))
    return sum/len(numbers)
c=average(9,4,4,3,3,2,32,43,34,4,3)
print(c)

'''def name(**name):


    print("hello",name["fname"], name["namsa"])

name(fname="bivbsbvib",namsa="jdfsjk")'''





