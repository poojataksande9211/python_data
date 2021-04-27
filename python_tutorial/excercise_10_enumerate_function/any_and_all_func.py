#any and all function
#write a program to check all eve no or not(by using all function)
# numbers1=[2,4,6,8,10]
# numbers2=[1,3,5,7,9]
# even_no=[]
# for num in numbers1:
#     if num%2==0:
#         even_no.append(True)
# print(even_no)
#-------------------------------
# even_no1=[]
# for num in numbers1:
#     even_no1.append(num%2==0)
# print(even_no1)
# print(all([True,True,True,True,True]))
#-------------------------------
#by using list comprehension and all function
numbers1=[2,4,6,8,10]
print(all([num%2==0 for num in numbers1]))
#-----------------------------------
#any function:any check any true no and print output true
numbers3=[1,53,10,5,43]
print(any([num%2==0 for num in numbers3]))

