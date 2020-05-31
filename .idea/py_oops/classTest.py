
class Computer:

    #basic function
    def config(self):
        print("config is",self.cpu,self.ram)

    #__init__ method
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

com1 = Computer('i5',16)
com2 = Computer('Ryzen 3',8)

com1.config()
com2.config()

