#list are mutable(we can change the list),and tuple are immutable
# l1=[1,"pooja",3.14,True,2-1j]
# print(l1)
# print(type(l1))
# print(l1[0])
# print(l1[-1])
# print(l1[2:5])
#modifing a list
l1=[1,"pooja",3.14,True,2-1j]
l1[0]=100 #replace 1 to 100
print(l1)
l1.append(87.90) #add new element at last
print(l1)
l1.pop() #remove last element
print(l1)
#-----------------------------
l2=["pooja",42,45,56,67.99,True,False]
l2.reverse() #reverse func
print(l2)
l2.insert(5,"hello") #inserting new element
print(l2)
#-----------------------------------
# l2=['v','a','g','h','o','r','x','z','p']
# l2.sort()
# print(l2)
#--------------------------------------
#concatinating two string
l1=['pooja','amit','ganvir']
l2=['banana','apple','dalimb']
print(l1+l2)
#repeating list 5 times and add list 1
print(l2*5 +l1)
