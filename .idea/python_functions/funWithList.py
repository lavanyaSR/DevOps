# passing list to function
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst = [10,23,34,36,47,56,67,78]
count(lst)
print("Even count: {} and Odd count: {}".format(even,odd))

