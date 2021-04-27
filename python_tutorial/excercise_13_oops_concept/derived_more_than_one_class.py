#1 can we derived more than 1 class...yes smartphon1 and smartphone2
class Phone:#base class/parent class
    def __init__(self,model_name,brand,price):
        self.model_name=model_name
        self.brand=brand
        self._price=max(price,0)

    def full_name(self):
        return f"{self.model_name} {self.brand}"

    def caliing_no(self,phone_no):
        return f"calling from {phone_no}"   
class Smartphone1(Phone):#derived class/child class
    def __init__(self,model_name,brand,price,ram,internal_memory,rear_camera):
        Phone.__init__(self,model_name,brand,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera

class Smartphone2(Phone):#derived class/child class
    def __init__(self,model_name,brand,price,ram,internal_memory,rear_camera):
        # Phone.__init__(self,model_name,brand,price)
        super().__init__(model_name,brand,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera

p1=Phone("nokia","34rff",8999)
p2=Smartphone2("1+","e3455gf",30000,4,56,"3t")
print(p2.full_name())