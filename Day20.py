#While loops
x= 1;

while(x<=10):
    print( x, " ", end="")
    x+=1
print("Done")

# Start pattern
# *
# * *
# * * * 
# * * * *

i=1
j=1
while(i<=4):
    while(j<=i):
        print("* ", end="")
        j+=1
    j=1
    i+=1
    print()

print("Done")

