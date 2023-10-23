#Lists
nums = [10,20,30,40, "ABC"]

print(nums)

names = ["ACD", "Anik", "Maruf", "Monem"]

combined = [nums, names]
print(combined)

nums.append("50")
nums.insert(2, 77)

print(nums)

nums.pop()
nums.pop()

print(nums)
print(min(nums))
print(min(names))  #counts the characters