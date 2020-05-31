

class A:
    # below is constructor
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("in feature 1 ")

    def feature2(self):
        print("in feature 2 ")

#class B inheriting class A
class B(A):
    # this calls even A is super it still calls B class constructor if want to use A constructor then we need to use super word
    def __init__(self):
        super().__init__()
        print("in B init ")

    def feature3(self):
        print("in feature 3 ")
    def feature4(self):
        print("in feature 4 ")

a1 = B()