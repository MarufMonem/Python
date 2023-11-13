# userinput = int(input("Enter a number: "))

#Call method

def fact(userinput):
    response = userinput
    if(userinput>1):
        response = response * fact(userinput-1)
        return response
    else:
        return response
    

# print(fact(userinput))


def factOpt(userinput2):
    if(userinput2==1):
        return 1
    else:
        return userinput2 * factOpt(userinput2-1)
    
print(factOpt(5))