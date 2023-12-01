#wap to remove the empty tuples from a given list of

lst=[(),(),('',),(),(34,2,4),([],),()]
for i in lst:
    if i == ():
        lst.remove(i)
print(lst)


