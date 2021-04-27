#write a python code to clone or copy a list
# def colone_list(l):
#     clone_copy=l.copy() #by using copy method
#     return clone_copy
# num=[1,2,3,4,5]
# print(colone_list(num))
#-------------------------------
def colone_list(l):
    clone=[]
    for i in l:
        clone.append(i) #clone using append method
    return clone
num=["pooja","amit","niven"]
print(num)
print(colone_list(num))
