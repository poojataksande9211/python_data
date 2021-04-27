#list comprehension with if statement
numbers=list(range(1,11))
print(numbers)
# new_list=[]
# for i in numbers:
#     if i%2==0:
#         new_list.append(i)
# print(new_list)
#---------------------
new_list=[i for i in numbers if i%2==0] #even
new_list_even=[i for i in range(1,11) if i%2==0]
print(new_list)
print(new_list_even)
#-----------------------------
odd=[i for i in range(1,11) if i%2 != 0]
odd1=[i for i in numbers if i%2 !=0]
print(odd)
print(odd1)