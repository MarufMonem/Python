# break, continue and pass

# for loops
limit = int(input("How many candies do you want?\n"))

count =0

while(count<limit):
    print("Candy")
    count+=1
    if count>6:
        print("Out of stock")
        break