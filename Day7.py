# Dictionary

# New dict
data = {1:"Maruf", 2:"Monem", 10:"Anik"}
print(data[10])

# Merge lists to a dictionary
key = ["M", "A", "P"]
val = ["Maruf", "Anik", "Python"]
dictionary = dict(zip(key, val))
print(dictionary)

# Add new items to a dict
dictionary["N"] = "Navin"
dictionary["J"] = "Java"
print(dictionary)

# remove items
del dictionary["P"]
dictionary.pop("J")

print(dictionary)

