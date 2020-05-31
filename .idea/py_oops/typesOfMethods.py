#instance method, class method and static method

class Student:

    school = 'WGL'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    #instance method
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    #class method
    @classmethod
    def getschool(cls):
        return cls.school

    #static method
    @staticmethod
    def info():
        print("this is student class in static module")

s1 = Student(67,78,89)
s2 = Student(90,89,78)
print()
print(s1.avg())
print(Student.getschool())
Student.info()

