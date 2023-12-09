phone={
"jhone":5424,
"ria":324,
"hasani":324324
}

#print the dictionary
print(phone)

#checking type of dictionary
print(type(phone))

#check the lenght of dictionary
print(len(phone))

#access items of dictionary
print(phone["jhone"])

print(phone.keys())

#update value in dictionary
phone["jhone"]=898989898989898989898

print(phone)

#add elements in dictionary
phone["john"]=7878787878
print(phone)


#nested dictionary

more_phone={"kia": 67676
           }
phone.update(more_phone)
print(phone)


#remove elemnets from phone
phone.pop("jhone")
print(phone)

#clear the list
phone.clear()
print(phone)

#printing elements of a dictionary
for x,y in phone.items():
    print(x,y)







#nested dictionary

