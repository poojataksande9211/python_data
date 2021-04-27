#map function
numbers=[1,2,3,4,5]
def square(a):
    return a**2
# squars=list(map(square,numbers))
# print(squars)
#-----------------------------------
#by using list comprehension
# numbers=[1,2,3,4,5]
# squars_2=[i**2 for i in numbers]
# print(squars_2)
#--------------------------
# numbers=[1,2,3,4,5]
nwe_list=[]
# def square(a):
#     nwe_list=[]
#     return a**2
for num in numbers:
    nwe_list.append(square(num))
print(nwe_list)
#---------------------------
#------------------------------
# names=['abc','abcd','abcde']
# length=map(len,names)
# print(length)
# for i in length: #map object pe 1 hi bar loop chala sakte h
#     print(i)
#--------------------------------------
names=['abc','abcd','abcde']
length=list(map(len,names))
print(length)