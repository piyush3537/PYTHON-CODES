#lamda function

'''add= lambda a,b:a+b
out = add(2,4)
print(out)

#wrt a lamba function to convert celcius to equivalent faherenite

f=lambda c: (c*1.8)+32
out=f(100)
print(out)

#lambda with sorting

def apna_fun(st):
    s=0
    for  i in st:
        s+=ord(i)
        return s
ls=['piyush','zooya','hyna']
print("before sorting",ls)
ls.sort(key=apna_fun)
print('after sorting',ls)'''


#lambda with sorting # here we are talking about ASCII value

'''ls=['piyush','zooya','hyna']
print("before sorting",ls)
ls.sort(key=lambda st:sum([ord(i) for i in st]))
print('after sorting',ls)'''


#lambda with mapping
'''ls=['piyush','zooya','hyna','uvy']
print("before mapping",ls)
out=list(map(lambda st: st.capitalize(),ls))
print('after mapping',out)'''


#lambda with mapping
def add_2(n):
    return n+3
lst = [4,6,7,8]
print('before mapping',lst)
out = list (map(lambda n: n+3,lst))
print('after mapping',out)

#lambda with mapping ....diiffer
def add_2(n):
    return n%2 ==0
lst = [4,6,7,8]
print('before mapping',lst)
out = list (map(lambda n: n%2,lst))
print('after mapping',out)



