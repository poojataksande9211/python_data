#write a python program to print even no multiply by 2 and odd no negative
list1=[1,2,3,4,5,6,8,9] #without list comprehension
new_list=[]
for i in list1:
    if i%2==0:
        new_list.append(i*2)
    else:
        new_list.append(-i)
print(new_list)
#-----------------------------------------
new_list1=[i*2 if i%2==0 else -i for i in list1] #with comprehension
print(new_list1)