def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
        return s
##main code
dct={}
while 1:
    num=int(input("enter the number"))
    out=fact(num)
    print(f'factorial of given number{num} is{out}')
    dct[num] = out
    print("do you want continue y/n")
    if input() !="y":
      print(f"your all result {dot}")
    break