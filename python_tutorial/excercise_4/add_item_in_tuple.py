#Write a Python program to add an item in a tuple.
num=1,2,3,4,5,8,0,9
print(num) #we can not add item to the tuple
num=num+(9,) #by using merge of tuple +operator add item to the tuple
print(num)
#adding item in a specific index
num=num[:5]+(10,20,30)+num[:5]
print(num)
listx=list(num)
listx.append(30)
print(listx)
num=tuple(listx)
print(num)
