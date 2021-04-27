#inheritance
class Phone:#base class/parent class
    def __init__(self,model_name,brand,price):
        self.model_name=model_name
        self.brand=brand
        self._price=max(price,0)
    def full_name(self):
        return f"{self.model_name} {self.brand}"
    def calling_no(self,phone_no):
        return f"calling {phone_no}"

class Smartphone(Phone):#derived class/child class
    def __init__(self,model_name,brand,price,ram,internal_memory,rear_camera):
        Phone.__init__(self,model_name,brand,price)
        # super().__init__(model_name,brand,price) #same as above method to call parent class
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera
        
p1=Phone("nokia","567f",980)
p2=Smartphone("1+","17vggfhmzz",34000,3,4,"3ds")
print(p1.full_name())
print(p2.full_name())
print(p2.__dict__)
print(p2._price)
