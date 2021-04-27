#class method
#diff between class method and instance method
class Person:
    count_instance=0 #class variable/class atribute
    def __init__(self,name,midd_name,sir_name,age):
        Person.count_instance+=1
        self.name=name
        self.midd_name=midd_name
        self.sir_name=sir_name
        self.age=age
    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instance of person class"
p1=Person("pooja","amit","ganvir",29)
p2=Person("amit","dushant","ganvir",33)
print(Person.count_instances())