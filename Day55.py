# Parent class definition
class Parent:
    def location(self):
        print("In class parent")
    
    def parentUniqueFeature(self):
        print("Earns money")

# Child class inherits from Parent class
class Child(Parent):
    def location(self):
        print("In class child")
    
    def childUniqueFeature(self):
        print("Goes to school")

# GrandChild class inherits from Child class
class GrandChild(Child):
    def location(self):
        print("In the grandchild class")
    
    def grandchildUniqueFeature(self):
        print("Doesn't go to school yet")

# Creating an instance of the Parent class
person1 = Parent()

# Calling the location method of the Parent class
print(person1.location())  # Output: In class parent
# Calling the parentUniqueFeature method of the Parent class
print(person1.parentUniqueFeature())  # Output: Earns money

# Attempting to call the childUniqueFeature method of the Child class on an instance of the Parent class
# This would give an error since childUniqueFeature is not defined in the Parent class
# Uncommenting the line below would result in an AttributeError
# print(person1.childUniqueFeature())

# Creating an instance of the Child class
person2 = Child()

# Calling the location method of the Child class
print(person2.location())  # Output: In class child
# Calling the childUniqueFeature method of the Child class
print(person2.childUniqueFeature())  # Output: Goes to school
# Calling the parentUniqueFeature method of the Parent class on an instance of the Child class
# Since Child inherits from Parent, it can access methods of the Parent class
print(person2.parentUniqueFeature())  # Output: Earns money

# Multiple inheritance: Creating an instance of the GrandChild class
person3 = GrandChild()

# Calling the location method of the GrandChild class
print(person3.location())  # Output: In the grandchild class
# Calling the grandchildUniqueFeature method of the GrandChild class
print(person3.grandchildUniqueFeature())  # Output: Doesn't go to school yet
# Calling the childUniqueFeature method of the Child class on an instance of the GrandChild class
# Since GrandChild inherits from Child, it can access methods of the Child class
print(person3.childUniqueFeature())  # Output: Goes to school
