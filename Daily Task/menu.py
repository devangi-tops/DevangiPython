print("-----Choice Board-----")
def again():
    answer=input("D0 you want anything else ? [y/n]")
    if answer == "y":
        print("OK")
        menu()
    elif answer == "n":
        print("Thank You")

def menu():
    print("1.Addition :- ")
    print("2.substraction :- ")
    print("3.Multiplication :- ")
    print("4.Divion :- ")
    print("5.Modulo :- ")
    print("6.exit")

    choice=int(input("Enter the choice :- "))
    if choice==1:
        addition()
        again()
    elif choice==2:
        substraction()
        again()

def substraction():
    a = int(input("Enter the number 1 :- "))
    b = int(input("Enter the number 2 :- "))

    c = a-b

    print(c)

def multiplication():
    a = int(input("Enter the number 1 :- "))
    b = int(input("Enter the number 2 :- "))

    c = a*b

    print(c)

def divion():
    a = int(input("Enter the number 1 :- "))
    b = int(input("Enter the number 2 :- "))
   
    c = a/b

    print(c)
