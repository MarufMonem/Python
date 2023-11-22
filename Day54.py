#Inner class

class OuterClass_Uni:

    def __init__(self, name, location, year) -> None:
        self.uniName = name
        self.uniLocation = location
        self.year = year
        self.student = self.InnerClass_Studnet("Constant Name", 0) # we can also do this 

    class InnerClass_Studnet:
        def __init__(self, name, id) -> None:
            self.studentName = name
            self.studentID = id

bracU = OuterClass_Uni("Brac University", "Dhaka", 2006)
print(f"University Name: {bracU.uniName} is located in {bracU.uniLocation} and was established in {bracU.year}")

bracuStudent = bracU.InnerClass_Studnet("Maruf", 10)
print(f"Student name is: {bracuStudent.studentName} and ID is: {bracuStudent.studentID}")

bracuStudent2 = OuterClass_Uni.InnerClass_Studnet("Monem", 20)
print(f"Student name is: {bracuStudent2.studentName} and ID is: {bracuStudent2.studentID}")

uiu = OuterClass_Uni("UIU", "Madani", 2001)
print(f"University Name: {uiu.uniName} is located in {uiu.uniLocation} and was established in {uiu.year}. The student details are: {uiu.student.studentName} & {uiu.student.studentID}")
