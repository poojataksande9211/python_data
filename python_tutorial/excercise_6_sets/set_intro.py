#what is set:unordered collecton of unique items,we can not store list,tuple,dictionary in set
s={1,2,3,4,3,3} #repeated value count only at once
print(s)#in set there is no key value
#-----------------------
#suppose we want to replace unique item in list use set method
l=[1,2,3,4,5,6,4,4,4,5,6,4,8,9,2]
# sa=set(l)
sa=list(set(l))
print(sa)
#----------
#add data to set
s1={1,2,3,4,5}
s1.add(6)
s1.add(7)
s1.add(6)
print(s1)
# remove method
s1.remove(4)
print(s1)
#clear() method
# s1.clear()
# print(s1)
#copy method
s1_copy=s1.copy()
print(s1_copy)
#----------------
s2={1,1.0,2.9,"pooja","AMIT"}#1.0 not print bcoz 1.0 treat as 1
print(s2)