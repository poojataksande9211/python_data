#genwrator comprehension
# square=[i**2 for i in range(1,11)] #list comprehension
square=(i**2 for i in range(1,11)) #generator comprehension
for i in square:
    print(i)
for i in square:
    print(i)
#-----------------------------
# square=(i**2 for i in range(1,11))
# print(next(square))
# print(next(square))
# print(next(square))
# print(next(square))