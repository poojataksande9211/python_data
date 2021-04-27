#args with normal parameter
# def multiply(*args): #parameter
#     multiply=1
#     for i in args:
#         multiply *=i
#     return multiply
# print(multiply(1,2,3,4)) #argument
#----------------------------
# def multiply(num,*args): #parameter
#     multiply=1
#     # print(num)
#     # print(args)
#     for i in args:
#         multiply *=i
#     return multiply
# print(multiply(2,2,3)) #(first 2 is not a part of args its a part of num)
#-------------------------------------
# def multiply(num,*args): #parameter #########
#     multiply=1
#     # print(num)
#     # print(args)
#     for i in args:
#         multiply *=i
#     return multiply
# print(multiply())#it gives an error(you have to pass 1 argument bcoz u define parameter num)
#---------------------------------
def multiply(num1,num2,*args): #parameter
    multiply=1
    # print(num)
    print(args)
    for i in args:
        multiply *=i
    return multiply
print(multiply(2,2,3,4)) #you pass 2 parameter hence u have to pass 2 argument