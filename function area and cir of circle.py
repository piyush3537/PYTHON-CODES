#waf to calculatr area and circumference circle
def area_of_circle(r):
    a=3.14*r*r
    return a
def circumference_of_circle(r):
    c=2*3.14*r
    return c
##main code
radius=int(input("enter the radius"))

area=area_of_circle(radius)
circumference=circumference_of_circle(radius)

print(f'area_of_rectangle{area}')

print(f'circumfrence of circle {circumference}')