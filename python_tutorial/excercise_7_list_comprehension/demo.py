# sq=[]
# for i in range(1,11):
#     sq.append(i**2)
# print(sq)
# sq1=[i**2 for i in range(1,11)]
# print(sq1)
# neg=[]
# for i in range(1,11):
#     neg.append(-i)
# print(neg)
# neg1=[-i for i in range(1,11)]
# print(neg1)
# list1=['pooja','amit','raj']
# list2=[]
# for i in list1:
#     list2.append(i[0])
# print(list2)
# list3=[i[0] for i in list1]
# print(list3)
# list1=['str1','pooja','amit']
# list2=[]
# for i in list1:
#     a=i[::-1]
#     list2.append(a)
# print(list2)
# list3=[i[::-1] for i in list1]
# print(list3)
# numbers=list(range(1,11))
# list1=[]
# for i in numbers:
#     if i%2==0:
#         list1.append(i)
# print(list1)
# list2=[i for i in numbers if (i%2==0) ]
# print(list2)
# odd=[i for i in range(1,11) if i%2!=0]
# print(odd)
# odd1=[i for i in numbers if i %2!=0]
# print(odd1)
# def num(l):
#     dd=[]
#     for i in l:
#         if type(i)==int or type(i)==float:
#             dd.append(str(i))
#     print(dd)
# num([True,False,[1,2,3,4],'pooja',2,4.0,8,22,'amit',"raj"])
def num(l):
    dd=[str(i) for i in l if type(i)==int or type(i)==float]
    print(dd)
num([True,False,[1,2,3,4],'pooja',2,4.0,8,22,'amit',"raj"])