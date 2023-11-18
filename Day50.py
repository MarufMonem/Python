class computer:
    cpuName = "M1"
    def __init__(self, cpu, ram):
        print("In the constructor")
        self.cpuName = cpu
        self.ramCount = ram


    def method1(self):
        print("Inside method 1")
        print(self.cpuName + " " + self.ramCount)
        print("Class variable: " + computer.cpuName)

obj = computer("i5", "16GB")
obj.method1()