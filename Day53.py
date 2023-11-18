class Student:
    # Class variables
    uniName = "BracU"
    uniDeptCount = 10

    # Constructor
    def __init__(self, listOfNumbers) -> None:
        # Instance variable to store test results
        self.allResults = listOfNumbers

    # Instance method to calculate average mark
    def averageMark(self):
        sum = 0
        for i in self.allResults:
            sum += i
        average = sum / len(self.allResults)
        return average
    
    # Class method to get university department count
    @classmethod
    def getUniDeptCount(cls):
        return cls.uniDeptCount
    
    # Class method to set university department count
    @classmethod
    def setUniDeptCount(cls, val):
        cls.uniDeptCount = val
    
    # Instance method to set updated test results
    def setallResults(self, updatedResults):
        self.allResults = updatedResults

    # Instance method to get all test results
    def getallresults(self):
        return self.allResults
    
    # Static method to close the testing process
    @staticmethod
    def closeProcess():
        print("Tests are completed")

# Creating instances
maruf = Student([70, 80, 90])
anik = Student([70, 70, 70])

# Printing information
print(f"Departments: {Student.uniDeptCount}")
print(f"University Name: {maruf.uniName}, Average Mark: {maruf.averageMark()}")
print(f"University Department Count: {Student.getUniDeptCount()}")
print(f"Maruf's University Department Count: {maruf.getUniDeptCount()}")

print(f"\nUniversity Name: {maruf.uniName}, Average Mark: {anik.averageMark()}")
print(f"Anik's current results: {anik.getallresults()}")
anik.setallResults([90, 90, 90])
print(f"Updated results for Anik: {anik.averageMark()}")

anik.setUniDeptCount(12)
print(f"Departments: {Student.uniDeptCount}")

# Closing the testing process
Student.closeProcess()
