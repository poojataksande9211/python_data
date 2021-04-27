#decision making sentence
# a=10
# b=20
# if(b>a):
#     print("b is greater than a")
# if (a>b):
#     print("a is greater than b")
# else:
#     print("b is greater than a")
#------------------------------------
# a=45
# b=21
# c=20
# if (a>b) & (a>c):
#     print("A is the greatest")
# elif (b>a) & (b>c):
#     print("B is the greatest")
# else:
#     print("C is the greatest")
#------------------------------
#if with tuple
# tup1=('a','b','c','d','e')
# if 'z' in tup1:
#     print("a is present in tup1")
# else:
#     print('z is not present in tup1')
#-------------------------
#if with list
# l1=['a','b','c']
# if l1[1]=='b':
#     l1[1]='z'
# print(l1)
#------------------------
#if with dictionary
d1={'k1':30,'k2':56,'k3':70,'k4':80}
if d1['k2']==56:
    d1['k2']=d1['k2']+100
print(d1)
