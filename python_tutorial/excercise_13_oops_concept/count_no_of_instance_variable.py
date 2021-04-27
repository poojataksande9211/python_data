#program to count instance variable
class Person:
    count_instance=0
    def __init__(self,name,midd_name,sir_name,age):
        Person.count_instance +=1
        self.name=name
        self.midd_name=midd_name
        self.sir_name=sir_name
        self.age=age
p1=Person("pooja","amit","ganvir",28)
p2=Person("amit","dushant","ganvir",32)
print(Person.count_instance)

