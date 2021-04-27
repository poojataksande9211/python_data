#Write a Python program to remove an item from a tuple
mixed=(1,2,3,4,5,6,"a","b",7) 
print(mixed)
mixed=mixed[:3]+mixed[4:]#tuples are immutable hence we can not remove...use merge operator create new tuple 
print(mixed)
listx=list(mixed) 
listx.remove(5)
listx=tuple(listx)
print(listx)