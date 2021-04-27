#class method as a constructor
#when we create instance init method call hoga,init method is a constructor which can create instances
class Person:
    count_instance=0
    def __init__(self,name,midd_name,sir_name,age):
        Person.count_instance +=1
        self.name=name
        self.midd_name=midd_name
        self.sir_name=sir_name
        self.age=age
    @classmethod
    def from_string(cls,string):
        name,mid,last,age=string.split(',')
        return cls(name,mid,last,age)
    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instance of class Person"
    def full_name(self):
        return f"{self.name} {self.sir_name}"
p1=Person("pooja","amit","ganvir",45)
print(p1.count_instances())
#supose we have to create our own object like p1=person("pooja,amit,ganvir,33")
p3=Person.from_string("pooja,amit,ganvir,33")
print(p3.full_name())