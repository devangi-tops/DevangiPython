print("-----Area Finder-----")

def mainMenu():
    print("1.circle")
    print("2.Triangle")
    print("3.Rectangle")
    find=int(input("Enter choice:- "))
    if find ==1:
        circle()
    elif find==2:
        triangle()
    elif find==3:
        rectangle()
    else:
        print("Invalid choice Enter 1-3")
        mainMenu()

def circle():
    r=int(input("Enter radius of circle = "))
    pi=3.14
    area=pi*r*r
    print("Area of given circle = ",area)

def triangle():
    h=int(input("Enter height of triangle = "))
    b=int(input("Enter base of triangle = "))
    area=(0.5)*h*b
    print("Area of triangle = ",area)

def rectangle():
    l=int(input("Enter length of Rectangle = "))
    b=int(input("Enter base of Rectangle = "))
    area=l*b
    print("Area of Ractangle = ",area)

mainMenu()

print("---Thank You---")
