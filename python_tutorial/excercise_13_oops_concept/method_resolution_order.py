#method resolution order
class Phone:#base class/parent class
    def __init__(self,model_name,brand,price):
        self.model_name=model_name
        self.brand=brand
        self._price=max(price,0)

    def full_name(self):
        return f"{self.model_name} {self.brand}"

    def caliing_no(self,phone_no):
        return f"calling from {phone_no}"   
class Smartphone(Phone):#derived class/child class
    def __init__(self,model_name,brand,price,ram,internal_memory,rear_camera):
        Phone.__init__(self,model_name,brand,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera

class flagshipPhone(Smartphone):
    def __init__(self,model_name,brand,price,ram,internal_memory,rear_camera,front_camera):
        Smartphone.__init__(self,model_name,brand,price,ram,internal_memory,rear_camera)
        self.front_camera=front_camera
p1=Phone("nokia","87hg",790)
p2=Smartphone("1+","67ytr",78000,"16gb","4gb","7mp")     
p3=flagshipPhone("1+","67ytr",78000,"16gb","4gb","7mp","9mp")
print(p3.full_name()) 
print(help(flagshipPhone))
#mro check fullname method present in flagship or not....suppose not then search fullname method in smartphon
#full name not present in smartphon then check in phone class