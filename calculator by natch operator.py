num1=int(input("enter the number 1"))
num2=int(input("enter the number 2"))

operator=input("enter the operator")
match operator:
    case"+":
            print("sum is",num1+num2)
    case"-":
            print("difference is",num1-num2)
    case"*":
            print("multiply is",num1*num2)
    case"/":
            print("quotient is",num1/num2)
    case _:
            print("enter a valid operator")
