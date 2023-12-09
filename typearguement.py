'''def average(a,b):
    print("the average:",(a+b)/2)
average(4,6)'''
#default arguement
#keyword arguements


def average(*numbers):
  sum=0
  for i in numbers:
    sum=sum+i
  print("average  is:",sum/len(numbers))
average(5,6,7,1)

