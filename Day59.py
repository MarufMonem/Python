class Student:

    # Constructor to initialize math and english scores
    def __init__(self, r1, r2) -> None:
        self.math = r1
        self.english = r2
        print("Total Score ", r1 + r2)

    # Method to compare math and english scores
    def compare(self):
        if self.math > self.english:
            print("Good at maths")
        else:
            print("Good at english")

    # Method overloading for ">"
    def __gt__(self, other):
        total1 = self.math + self.english
        total2 = other.math + other.english

        if total1 > total2:
            print("Student 1 is better")
        else:
            print("Student 2 is better")

# Creating instances of the Student class
s1 = Student(50, 60)
s2 = Student(50, 80)

# Calling the compare method on instances of the Student class
s1.compare()
s2.compare()

# Using the overloaded ">" operator
s1.__gt__(s2)
