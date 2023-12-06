def topTenVal():
    n =1
    while (n<=10):
        yield n
        n+=1

values =topTenVal()

for i in values:
    print(i)