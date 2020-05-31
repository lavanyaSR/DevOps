# inner class - used for Increased encapsulation - More readable, maintainable code

class College:

    def __init__(self):
        print("Outer class")

    class Student:
        def __init__(self):
            print("inner class")

        def displayS(self):
            print("student method")

    def displayC(self):
        print("College Method")


c = College()
c.displayC()
print()
#inner class can not be created by its object so need to point to outer class
s = c.Student()
s.displayS()
s.displayC()