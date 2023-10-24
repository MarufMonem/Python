# input

# x = int(input("Give val\n"))
y = int(input("Give a below for Y\n"))

print("Sum: ", x+y) # treating it as a string

# Eval function
result = eval(input("Input an expression"))
print(result)

# Arguments
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

print(a+b)