#wap to remove the empty tuples from a given list of

lst=[(),(),('',),(),(34,2,4),([],),()]
out=[]
for i in lst:
    if i!=():
        out.append(i)
        print(out)

