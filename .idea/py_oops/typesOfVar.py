
class Car:
    #class/ static variable
    wheels = 4

    def __init__(self):
        #instance variable
        self.model = 'BMW'
        self.mil = 10

c1 = Car()
c2 = Car()

c1.mil = 15

print(c1.model,c1.mil, c1.wheels)
print(c2.model,c2.mil, c2.wheels)

