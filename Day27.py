from array import *

length = int(input("Size of the array?\n"))

arr = array('i', [])

for i in range(length):
    print("What is the value for index ", i, ": ", end="")
    val = int(input())
    arr.append(val)

print(arr)

# Search for the values:
searchVal = int(input("What is the value?\n"))

count=0
for i in arr:
    if(i==searchVal):
        print(count)
        break
    count+=1
else:
    print("Not found")


# built in methods
print(arr.index(searchVal))
