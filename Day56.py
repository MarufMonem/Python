# Parent class definition
class Parent:
    # Constructor for the Parent class
    def __init__(self) -> None:
        print("Inside parent's constructor")

    # Method to print the location in the parent class
    def location(self):
        print("In class parent")
    
    # Method to print a unique feature of the parent class
    def parentUniqueFeature(self):
        print("Earns money")

# Child class inherits from Parent class
class Child(Parent):
    # Constructor for the Child class
    def __init__(self) -> None:
        # Calling the constructor of the parent class using super()
        super().__init__()
        print("Inside child's constructor")
    
    # Method to print a unique feature of the child class
    def childUniqueFeature(self):
        print("Goes to school")

# Another parent class
class StepParent:
    # Constructor for the StepParent class
    def __init__(self) -> None:
        print("Inside step parent's constructor")

    # Method to print the location in the step parent class
    def location(self):
        print("In class step parent")
        
    # Method to print a unique feature of the step parent class
    def stepParentUniqueFeature(self):
        print("Step parent")

# Child class inheriting from both Parent and StepParent classes
class StepChild(Parent, StepParent):
    # Method specific to StepChild class
    def grandchildUniqueFeature(self):
        print("Step child")

# Creating an instance of the Child class
personChild = Child()

# Calling the childUniqueFeature method of the Child class
print(personChild.childUniqueFeature())

# Creating an instance of the StepChild class
sc = StepChild()
# Calling the location method, which is present in both Parent and StepParent classes
print(sc.location())
