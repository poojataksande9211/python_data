#Write a Python program to check whether an element exists within a tuple. 
# mixed=(1,2,3,4,5,6,7,8)
# print(mixed)
# n=int(input("enter ele"))
# if n in mixed:
#     print(n,"exist")
# else:
#     print(n,"not exist")
#------------------------
mixed=(1,2,3,4,5,6,7,8,"pooja",4.0,"amit")
print("pooja" in mixed)
print(4 in mixed)
print(0 in mixed)
print(4.0 in mixed)