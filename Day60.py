from abc import ABC, abstractclassmethod

# Abstract class definition
class Computer(ABC):
    def __init__(self, name):
        self.name = name

    @abstractclassmethod
    def ram(self, size):
        pass
    
    def processor(self, name):
        pass
    
    def gpu(self, name, ram):
        pass
    
    def concrete(self):
        print(self.name)
        return "inside concrete class"

# Concrete class inheriting from the abstract class
class DesktopWork(Computer):
    # Implementing the abstract method for RAM
    def ram(self, size):
        return f"{size} GB"
    
    # Implementing the abstract method for processor
    def processor(self, name):
        return f"{name}"

    # Implementing the abstract method for GPU
    def gpu(self, name, ram):
        return f"{name} and has {ram} GB ram"

# Creating an instance of the concrete class
enosisPC = DesktopWork("enosisPc")

# Calling the concrete method of the concrete class
print(enosisPC.concrete())

# Calling the implemented methods of the concrete class
print(enosisPC.gpu("GTX1060", 6))
print(enosisPC.processor("i7"))
print(enosisPC.ram(8))
