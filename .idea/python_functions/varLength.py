# Variable length - add more than 2 numbers
def add(*b):
    c=0
    for i in b:
        c = c+i
    print(c)
add(1,3,56,78)