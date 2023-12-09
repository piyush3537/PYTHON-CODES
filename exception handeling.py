

#exception handeling:
'''a=input("enter the number")
print(f"multilicatiion table of {a} is:")
try:
  for i in range(1,11):

    print(f"{int(a)}X{i}={int(a)*i}")
except:
    print("hello humans")'''

#try except
'''try:
    b=int(input("enter b valuue"))
    print("this is a number")
except:
    print("this iss not a numbers")'''

#finally clause
try:
    l=[1,4,5,6]
    i=int(input("enter the index"))
    print(l[i])
except:
    print("some errror occcured")
finally:
    print("i am always executeed")

