userVal = int(input("Please enter a number to check\n"))

for i in range (2,userVal, 1):
    if(userVal%i==0):
        print("This is not a prime number")
        break
else:
    print("This is a PRIME number")