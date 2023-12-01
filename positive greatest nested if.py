num=int(input("enter a positive number"))
#checking whether is it divisible by 15
if num%15==0:
    print("number is divisible by 15")
else:
    #checking if divisible by 3 0r 5
    if num %3==0 or num%5==0:
        print ("number is not divisible by 5 or 3")
    else:
            print("number is neither divisible by 5 ,3")