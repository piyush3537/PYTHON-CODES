n=int(input("enter the number of days"))
year=(n/365)
weeks=(n%365)/7
days=(n%365)%7

print("total number of year")
print(year)
print("total number of weeks")
print(weeks)
print("total number of days")
print(days)