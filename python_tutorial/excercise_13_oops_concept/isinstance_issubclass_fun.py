#isinstance issubclass function
#instance means object
#isinstance :to check object is of perticular class
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
    def full_name(self): #overriding according to mro it will 1st present smartphone
        return f"{self.model_name} {self.brand} and price {self._price}"

class flagshipPhone(Smartphone):
    def __init__(self,model_name,brand,price,ram,internal_memory,rear_camera,front_camera):
        # Smartphone.__init__(self,model_name,brand,price,ram,internal_memory,rear_camera)
        super().__init__(model_name,brand,price,ram,internal_memory,rear_camera)
        self.front_camera=front_camera
    def full_name(self):
        return f"{self.model_name} {self.brand} and prize{self._price} front camera={self.front_camera}"
p1=Smartphone("1+","67ytr",78000,"16gb","4gb","7mp")
p2=flagshipPhone("1+","67ytr",78000,"16gb","4gb","7mp","9mp")
# print(p1.full_name())
# print(isinstance(p1,Smartphone))
# print(isinstance(p1,Phone))
# print(isinstance(p1,flagshipPhone))
# print(isinstance(p2,flagshipPhone))
# print(isinstance(p2,Smartphone))
# print(isinstance(p2,Phone))
print(issubclass(Smartphone,Phone)) #to check smartphon is a subclass of phone class
print(issubclass(Smartphone,flagshipPhone)) #smartphone is not sub class of flagshipPhone
print(issubclass(flagshipPhone,Smartphone)) #flagshipPhone is a subclass of smartphone
print(issubclass(flagshipPhone,Phone)) #flagshipphone is a subclassof phone
