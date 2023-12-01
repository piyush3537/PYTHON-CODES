'''list=[2,3,3,4]
print(list)
print(len(list))
print(type(list))

if "4" in list:
    print('yes present')'''


fruits=["banana","apple","l@@","juicy"]
print(fruits[-1])
print(fruits[1:3])
fruits.append("coal")
fruits.insert(3,"papaya")
print(fruits)

more_fruits=["apple","cheeze"]
fruits.extend(more_fruits)
#fruits.remove("banana")
#fruits.pop(2)
print(fruits)


#changing or updating items in list
'''fruits[1]="kiwi"
print(fruits)'''


fruits[1:3]=["rasberry"]
print(fruits)




#sorting a list

#fruits.sort(reverse=True)
fruits.reverse()
print(fruits)



#list comprehension
list=[1,2,2,33,44,52,25,2,626,26,26,27,28]
new_list=[i for i in list if i>25]
print(new_list)

new=new_list+fruits
print(new)

input=[23,65,19,90]
input[2]
















