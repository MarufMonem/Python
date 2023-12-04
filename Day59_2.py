# Method Overloading and Overriding

# Parent class definition
class Parent:
    # Method to get the phone brand for the parent
    def phone(self):
        return "Iphone"
    
# Child class (Student) inherits from Parent class
class Student(Parent):
    # Method to get the phone brand for the student
    def phone(self):
        return "Samsung"
    
    # Method to calculate total money, considering bank, cash, and bonds
    def totalMoney(self, bank=None, cash=None, bonds=None):
        # If all values are None, the person is considered broke
        if bank is None and cash is None and bonds is None:
            print("Broke")
            return 0

        # If bonds and cash are None, the person only has cash
        elif bonds is None and cash is not None:
            print("You only have cash")
            return cash
        
        # If bonds are None, the person can start investing with bank and cash
        elif bonds is None:
            print("Start investing")
            return bank + cash
        else:
            # If bonds are not None, the person doesn't have any cash and needs to go to the ATM
            print("You don't have any cash, go to the ATM")
            return bank

# Creating instances
father = Parent()
son = Student()

# Getting phone brand for parent and student
print(father.phone())
print(son.phone())

# To call the parent's method from the child class instance
print(super(Student, son).phone())
print("-------------------")

# Testing totalMoney method with different scenarios
totalAmountBroke = son.totalMoney()
print(totalAmountBroke)

totalAmountNoInvestment = son.totalMoney(100, 200)
print(totalAmountNoInvestment)

totalAmountNoCash = son.totalMoney(100)
print(totalAmountNoCash)
