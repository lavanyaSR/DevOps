# inheritence types:
# A-> B single level
# A -> B -> C : multi level
# C from both A and B multiple inheritence.


class A:
    def feature1(self):
        print("in feature 1 ")

    def feature2(self):
        print("in feature 2 ")

 #class B inheriting class A
class B(A):
    def feature3(self):
        print("in feature 3 ")
    def feature4(self):
        print("in feature 4 ")

a1 = A()
a1.feature1()
a1.feature2()

# can take method from class A. A is super class and B is sub class
b1 = B()
b1.feature1()
b1.feature4()