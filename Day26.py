# arrays
import array as a
valArray = a.array('i', [2,3,6,9,1,2,3])
# print(valArray)


# to get the type code
# print(valArray.typecode)
valArray.reverse()
print(valArray)

#Copying values from one array to another

newArray = a.array(valArray.typecode, (i for i in valArray))
print(newArray)