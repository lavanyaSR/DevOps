# with tuple ** kwargs - passing multiple arguments with the help of key words
def person(name,**kwargs):
    print(name)
    print(kwargs)

person('anya',age=34,city='SR',zip=34523,country='USA')
print()

def person1(name,**kwargs):
    print(name)
    for i,j in kwargs.items():
        print(i,j)

person1('anya',age=34,city='SR',zip=34523,country='USA')
