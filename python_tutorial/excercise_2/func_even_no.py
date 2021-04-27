#Write a Python program to print the even numbers from a given list.
# list1=[2,3,55,10,7,8,9,12,14,15] #without function
# for i in range(0,len(list1)):
#     if (list1[i]%2) ==0:
#         print(list1[i],end =" ")
#.....................
# list1=[2,3,55,10,7,8,9,12,14,15] #without function
# for i in list1:m
#     if (i%2) ==0:
#         print(i,end =" ")
#........................
def even_no(list):
    for i in list:
        if i%2 ==0:
            print(i,end =" ")
even_no([2,3,55,10,7,8,9,12,14,15])
