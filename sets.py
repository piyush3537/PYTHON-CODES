#creating a set
names={"sia","mia","nia","pia"}
#print set
print(names)

#accesing items in set
for x in names:
    print(x)

#check if present
if "sia"  in names:
    print("sia is in the set ")

    #add elements
    names.add("ria")
    names.add("sia")
    print(names)


#add another sequence in alist
names_list=["ria","kia"]
names.update(names_list)
print(names)




#joining 2 sets
s1={"a","b","c"}
s2={"e","r","f"}
print(s1,s2)
s3=s1.union(s2)
print(s3)

s1.update(s2)
print(s1)