#fromkeys() method  return a dictionary with the specified keys and specified values
# d=dict.fromkeys(['name','last_name','middle_name'],'unknown') #used list
# print(d)
# print(type(d))
#----------------------------
# d=dict.fromkeys(('name','middle_name','last_name'),'unknown') #used tuple
# print(d)
# print(type(d))
#--------------------------
# d=dict.fromkeys("pooja",'unknown') #use string itwill print seperately
# print(d)
#--------------------------
# d=dict.fromkeys(range(1,10),'unknown')
# print(d)
#--------------------------------
# d=dict.fromkeys(['name','age'],['unknown','unknown'])
# print(d)
#----------------------------------
#get method :=is used to access key
# d={'name':'unknown','age':'unknown'}
# print(d['name']) #it will print the key value of name
# print(d['names']) #it will give an error bocz names not present in dic to avoide this error use get method
# print(d.get('name'))#get method return the value of item with specified key
# print(d.get('names'))
#-----------------------------------
d={'name':'unknown','age':'unknown'}
# if 'name' in d:
#     print("present")
# else:
#     print("not present")
if d.get('name'):
    print("present")
else:
    print("not present")
#-------------------------
#clear() method removes all items from the dic
# d={'name':'unknown','age':'unknown'}
# d.clear()
# print(d)
#---------------------------------
# d={'name':'unknown','age':'unknown'}
# d1=d.copy()
# print(d1)
#------------------------------------
d={'name':'unknown','age':'unknown'}
# d1=d #its not copy of d(its aaign d value to d1,1 value delete from d1,it will delete from d also)
# print(d1.popitem()) 
# print(d)
# print(d1)
d1=d.copy()
print(d1.popitem()) #delete only from d1 not from d...d as it is
print(d1)
print(d)
#---------------------------
#check d and d1 are different
print(d1 is d) #ans false means both are diff