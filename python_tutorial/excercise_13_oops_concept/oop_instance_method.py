#oop instance method...instance/object
#class ke under jo bhi func he unko hum method bolate h
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def age_above_18(self):
        return self.age>18
p1=Person("pooja","ganvir",24)
p2=Person("amit","ganvir",16)
print(p1.full_name())
print(p2.age_above_18())
# print(Person.full_name(p1)) #same as above
#--------------------------------------------------------------
l=[1,2,3,4,5]
#clear and pop are method
# l.clear()
# list.clear(l) #same as above
# print(l)
# l.append(10)
list.append(l,10) #list is class name,same as above
print(l)