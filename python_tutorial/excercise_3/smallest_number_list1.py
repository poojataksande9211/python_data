#find the smallest element in list
# def smallest_num(l):
#     return min(l)
# number=[1,3,5,-9]
# print(smallest_num(number))
#-------------------------------
# def smallest_num(l):
#     small=l[0]
#     for i in range(len(l)):
#         if l[i]<small:
#             small=l[i]
#     return small
# number=[6,3,5,10]   
# print(smallest_num(number))
#-----------------------------
def smallest_num(l):
    small=l[0]
    for i in l:
        if i< small:
            small=i
    return small
number=[6,3,5,10,-1]   
print(smallest_num(number))