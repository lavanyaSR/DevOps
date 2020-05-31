#duck typing, method overloading, nethod overriding and operator overloading
#
# duck typing,
# class PyCharm:
#     def execute(self):
#         print("compiling")
#         print("running")
#
# class MyEditor:
#     def execute(self):
#         print("spell check")
#         print("Convention check")
#         print("compiling")
#         print("running")
#
# class Laptop:
#     def code(self,ide):
#         ide.execute()
#
# ide = MyEditor()
#
# lap1 = Laptop()
# lap1.code(ide)


#operator overloading
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        m1 = self.m1 + other.m2
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)

        return s3

s1 = Student(78,87)
s2 = Student(99,88)

s3 = s1+s2
print(s3.m2)

#Python will not support method overloading

