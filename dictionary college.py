#wap to iterate over dictionaries using for loops
'''info={"name":"piyush"
'sunbject':"webtech"}
for i in info:
    print(i,info(i))'''



marks={"physics":3,
"english":2,
"math":4,
"python":5,
"webtech":"none"}
s=0
for i in marks:
    val=marks[i]
    if type (val)==int:
        s+=val
print('total marks',s)

print(marks)


