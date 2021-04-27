#intro to *args
# def total(a,b):
#     return a+b
# print(total(3,5))
#-------------------
# def total(a,b):
#     return a+b
# print(total(3,5,10,4)) #it gives an error to solve this problem use * operater
#--------------------
# def all_total(*args):
#     print(args)
#     print(type(args))
# all_total(1,2,3,4,5,5)
#---------------------
def all_totall(*args):
    total=0
    for i in args:
        total+=i
    return total
print(all_totall(1,2,3,4))
