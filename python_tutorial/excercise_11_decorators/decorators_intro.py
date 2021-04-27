#intro to decorators
# def square(a):
#     return a**2
# s=square(7)
# print(s)
#------------------
def square(a):
    return a**2
s=square #here we assing function to variable s....yahape func ko call nahi kar rahe...
print(s(7))  #s kam karega function ki tarah
print(s.__name__) #it will print name of s
print(s)  #both s and square at same laocation
print(square)