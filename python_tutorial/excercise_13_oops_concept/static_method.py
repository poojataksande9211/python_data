#static method
#self represents the object or instance,cls represents class 
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
    def full_name(self):
        return f"{self.name} {self.sir_name}"
    @classmethod
    def count_instances(cls):
        return f"u have created {cls.count_instance} instance of {cls.__name__}"
    @staticmethod
    def hello():
        print("hello,static method called")
Person.hello()
# p1=Person.from_string("pooja,amit,ganvir,33")
# print(p1.full_name())
#static method not be related to the class and object