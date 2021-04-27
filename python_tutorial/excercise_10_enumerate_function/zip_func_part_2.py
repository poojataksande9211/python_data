#zip_func_Part_2
# l1=[1,2,3,4]
# l2=[5,6,7,8]
l3=[(1,5),(2,6),(3,7),(4,8)] #convert l3 to l1 l2
#zip with * operator
# print(list(zip(*l3)))
# l1,l2=list(zip(*l3))
# print(list(l1))
# print(list(l2))
#----------------------------------------
#program for find greatest of l1 l2 pair
l1=[1,2,3,4]
l2=[5,6,7,8]
new_list=[]
for pair in zip(l1,l2):
    new_list.append(max(pair))
print(new_list)
