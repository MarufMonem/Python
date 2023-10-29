from numpy import *

arr1 = array([1,2,3,5,7,9])
print(arr1)
# Add 5 to each element
arr2 = arr1 + 10
print(arr2)

arr3 = arr1+arr2
print(arr3)

#Copying array
arr2 = array([1,2,3])
arr3= array([9,8,7])

# Shallow copy
arrayShallowCopy = arr2.copy()
print(arrayShallowCopy)

arr2[1]=7
print(arr2)
print(arrayShallowCopy)
