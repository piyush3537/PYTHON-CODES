''''info1=['jatin',34,'gla university']
info2=['94599595',4.5]

info1.extend(info2)

print(info1)
print("out")'''


info1={"name":"jatin",
    "roll_no":"73",
    "sec ":"A"}
info2={"name":"piyush"
    "roll_no":"45"
    "sec":"b"}

for i in info2:
    info1[i]=info2[i]
print(info1)