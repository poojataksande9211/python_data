# def fac():
#     x=7 #we can not use x variable out of func
#     return x
# def fac2():
#     print(x) #we can not acccess value of x in fun 2 #error
# fac2()
#........................
x=5 #global variable
def fuc():
    global x #suppose we want to change the value of global variabl in func use global
    x=7 #local variable
    return x
print(x)
print(fuc())
print(x) #error x not define #becoz the scope of x only in func


