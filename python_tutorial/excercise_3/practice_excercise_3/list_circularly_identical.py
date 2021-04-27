#Write a python program to check whether two lists are circularly identical. 
# def identical_cir(l1,l2): not working"error""
#     t=0
#     k=0
#     for i in l1:
#         t=t+i
#     return t
#     for j in l2:
#         k=k+j
#     return k
#     # if k==t:
# #         print("identical")
# #     print("not iden")   
# num1=[1,2,3]
# num2=[2,1,3]  

# print(identical_cir(num1,num2))
#-----------------------------------
# num1=[1,4,3]
# num2=[3,1,4]
# sum_1=sum(num1)
# sum_2=sum(num2)
# print(sum_1)
# print(sum_2)
# if sum_1==sum_2:
#     print("list are identical")
# else:
#     print("list not identical")
#-------------------------------------
def iden(l1,l2):
    sum_1=sum(l1)
    sum_2=sum(l2)
    if sum_1==sum_2:
        print("list are identical")
    else:
        print("list not identical")
num1=[1,4,3,6,7]
num2=[3,1,4,7,6]
iden(num1,num2)