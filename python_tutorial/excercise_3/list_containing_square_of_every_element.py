#define a function which will take list containing numbers as input
#and return list containing square of every element
# number=[1,2,3,4,5]
# def square_list(l):
#     square=[]
#     for i in l:
#         square.append(i*i)
#     return square
# print(square_list(number))
#-----------------------------------
def square_list(l):
    square=[]
    for i in l:
        square.append(i*i)
    return square
numbers=list(range(1,6))
print(square_list(numbers))
