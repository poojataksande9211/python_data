#func return two values
def func(int1,int2):
    add=int1+int2
    mult=int1*int2
    return add,mult
# print(func(2,3)) #return one tuple
add,mult=func(2,3)
print(add)
print(mult)