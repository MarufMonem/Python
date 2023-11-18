def welcome():
    print("Hello user")

if(__name__ == "__main__"):
    print("In the main function")
    welcome()
else:
    print("Already logged in. Function name:  ", __name__ )