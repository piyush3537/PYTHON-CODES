from random import *
c_num=randrange(1,101)
chanes=5
while 1:

    u_num=int(input())
    if u_num ==c_num:
        print("you win")
        break
    elif u_num>c_num:
        print("too long")

    else:
        print("too small")



 chances-=1
        if chances<=0:
            print("you loose")
            break