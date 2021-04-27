#Write a Python program to append a list to the second list.
# def list_append(l1,l2):
#     for i in l1:
#         l2.append(i)
#     return l2
# list1,list2=[1,2,3],["a","b","c"]
# print(list_append(list1,list2))
#---------------------------
def list_append(l1,l2):
    return l1+l2
list1=["a","b","c"]
list2=[1,2,3]
print(list_append(list1,list2))