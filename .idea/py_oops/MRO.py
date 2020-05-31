# method resolution order always will be from left side, Example C is =inheriting from A and B it always gives pref to class A

class A:
    # below is constructor
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("in feature 1 in A ")

    def feature2(self):
        print("in feature 2 ")

#class B inheriting class A
class B():
    # this calls even A is super it still calls B class constructor if want to use A constructor then we need to use super word
    def __init__(self):
        super().__init__()
        print("in B init ")

    def feature3(self):
        print("in feature 3  in B")
    def feature4(self):
        print("in feature 4 ")


# class C(A,B):
#     #initially it calls class C constructor when it is not inheriting from A and B
#     def __init__(self):
#         print('in C init')
class C(A,B):
    def __init__(self):
        #it only takes from class A
        super().__init__()
        print('in C init')

    def feat(self):
        super().feature2()


a1 = C()
a1.feature1()
a1.feat()