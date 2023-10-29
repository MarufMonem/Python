def greet(a):
    print("Hello user")
    evenOrOdd(a)

def evenOrOdd(a):
    if userVal%2 == 0:
        print("Even")
    else:
        print("Odd")
    name = askForName()
    print("Thanks, ", name)

def askForName():
    name = input("Name: ")
    return name

def multiReturn (x,y):
    return x+5, y+10


userVal = int(input("input number: "))
greet(userVal)
x,y = multiReturn(10,20)
print(x,y)