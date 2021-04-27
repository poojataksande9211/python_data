#what is list comprehension
# sq=[]
# for i in range(1,11):
#     sq.append(i**2)
# print(sq)
#-------------
# sq2=[i**2 for i in range(1,11)]
# print(sq2)
#---------------------------------------
# neg=[]
# for i in range(1,11):
#     neg.append(-i)
# print(neg)
# #---
# neg2=[-i for i in range(1,11)]
# print(neg2)
#------------------------------------------
list1=['pooja','amit','Raj']
new_list=[]
for i in list1:
    new_list.append(i[0])
print(new_list)
#---
list1=['pooja','amit','Raj']
new_list1=[i[0] for i in list1]
print(new_list1)
#-----------------------------------------