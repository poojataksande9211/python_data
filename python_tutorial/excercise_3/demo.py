#list chapter summery
#list=list is a data structure that can hold any type of data
#create a list
words=["word1","word2"]
#u can store anything insight list
#----------------------------------------
# mixed=[1,2,3,[4,5,6],"seven",8.0,None] #None is a special value
# #list is a ordered collection of items
# print(mixed[0])
# print(mixed[3])
#-------------------------------------------
#add data to our list
mixed=[1,2,3,[4,5,6],"seven",8.0,None] #None is a special value
mixed.append("10")
print(mixed)
#------------------------------------------
#add complete list to list
mixed=[1,2,3,[4,5,6],"seven",8.0,None]
mixed.append([10,20,30])
mixed.append([40,50,60])
print(mixed)
#-----------------------------------------
mixed=[1,2,3,[4,5,6],"seven",8.0,None]
mixed.extend([10,20,30]) #extend can not add complete list....extend add only individual element to the list
print(mixed)
#----------------------------------------
#join two list
word1=["a,b,c,d"]
word2=["e,f,g,h"]
c=word1+word2
print(c)
#-------------------------------------
#insert 
mixed=[1,2,3,[4,5,6],"seven",8.0,None]
mixed.insert(1,"pooja") #add element to a specific position
print(mixed)
#--------------------------------------
#remove element from list
mixed=[1,2,3,[4,5,6],"seven",8.0,None]
pop_item=mixed.pop() #remove last element from list
print(pop_item) #return deleted element
print(mixed)
mixed.pop(2) #remove element at second pos
print(mixed)
#------------------------------------
#remove method:u want to remove element but u didnt know the position in that case remove method use
mixed=[1,2,3,[4,5,6],"seven",8.0,None]
mixed.remove("seven")
print(mixed)
#-------------------------------------
#del statement
mixed=[1,2,3,[4,5,6],"seven",8.0,None]
del mixed[3] #delete element at 3 pos
print(mixed)
#-------------------------------------
#looping in list
for i in mixed:
    print(i)

