eng_marks=int(input("enter the marks"))
maths_marks=int(input("enter the marks"))
if eng_marks>80 and maths_marks>80:
    print("grade a")
elif maths_marks>80 or eng_marks>80:
    print("grade b")
else:
    print("c grade")
