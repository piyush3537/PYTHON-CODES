#creating a tuple
colours = ("red","yellow","green")
print(colours)
#creating a tuple with 1 item
fruits=("apple",)

#check type tuple
print(type(fruits))
print(len(colours))

#aceesing item in a tuple
print(colours[0])

#range indexing
print(colours[0:3])

#check if an item exists in tuple
if "green" in colours:
    print("grreen is a part of colours")

#traverse the tuple
for i in colours:
    print(i)
 #concatenation

more_colours= ("blue","brown")
colours=colours+more_colours
print(colours)

#unpacking a tuple
colour1,colour2,colour3 = colours
print(colour1,colour2,colour3)


