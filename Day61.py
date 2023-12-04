listOfValues = {0,1,2,3,4,5,6,7,8,9}

it = iter(listOfValues)

for i in range(0,10,1):
    print(it.__next__())