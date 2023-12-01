#waf to calculatr area and perimeterde
def area_of_rectangle(l,b):
    a=l*b
    return a
def peri_of_rect(l,b):
    p=2*(l+b)
    return p
##main code
length=int(input("enter the length"))
breadth=int(input("enter the breadth"))
area=area_of_rectangle(length,breadth)
peri=peri_of_rect(length,breadth)

print(f'area_of_rectangle{area}')

print(f'perimeter of the rectangle{peri}')