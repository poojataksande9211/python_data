#tuple is an orderd collection of elements enclosed within ()
#tuples are immutable(means u cant change tuple element) and u can store different types of elements
tup1=("pooja",13,3.24,1+3j)
print(tup1)
print(type(tup1))
#extacting individual elements in tuple
print(tup1[0])
print(tup1[-1])
print(tup1[1:3])
#-----------------
print(len(tup1))
tup2=(2,3,4,5)
tup3=(6,7,8,9)
print(tup2,tup3)
print(tup2+tup3) #concatinate two string
#repeating tuple element
print(tup1*5)
print(tup2*2+tup3)
#-----------------------------
tup4=(10,20,30,40,1,2,3)
print(max(tup4))
print(min(tup4))