#create your first class
#init method is called as constructor
#in class func define is called method
class Person: #class
    def __init__(self,first_name,last_name,age): #attribute
        print('init method / constructor get called') #3 time init method call
        #instance variable
        self.first_name=first_name #self represent the objct
        self.last_name=last_name
        self.age=age
p1=Person("pooja","ganvir",34) #object
p2=Person("harshit","vaishishth",23)
p3=Person("rajan","pradhan",34)
print(p1.first_name)
print(p2.first_name)
print(p3.first_name)