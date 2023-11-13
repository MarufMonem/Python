import sys

# Recursion limit
print(sys.getrecursionlimit())

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

def greet():
    print("hello")
    greet()

# greet()