#list comprehension summury
square=[]
for i in range(1,11): #without list comprehension
    square.append(i**2)
print(square)
#-------------
square1=[i**2 for i in range(1,11)] #with list comprehenion
print(square1)
#......................................
#if condition in list comprehension
even_no=[i for i in range(1,11) if i%2 ==0]
print(even_no)
#------------------------------------
#list comprehension with if else(even no multi by 2 and odd no mult by -1)
mixed=[i*2 if (i%2==0) else -i for i in range(1,11)]
print(mixed)
#---------------------------------
#nested list comprehension
nl=[[1,2,3],[1,2,3],[1,2,3]]
nested_list=[[i for i in range(1,4)] for j in range(3)]
print(nested_list)
# new_l=[] #without list comprehension
# for j in range(3):
#     new_l.append([1,2,3])
# print(new_l)
