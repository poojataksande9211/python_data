#special_magic/dunder method...starting and ending with double under_score ex..(__init__)
#pollymorphisom...ex method overriding
# class Phone:
#     def __init__(self,brand_name,model,price):
#         self.brand_name=brand_name
#         self.model=model
#         self.price=price
#     def phone_name(self):
#         return f"{self.brand_name} {self.model}"
#     def __repr__(self):
#         return f"{self.brand_name} {self.price}"
#     def __str__(self):
#         return f"{self.brand_name} {self.model} {self.price}"
#     def __len__(self):
#         return len(self.phone_name())
#     def __add__(self,other):
#         return self.price + other.price
# # l=[1,2,3]
# # print(l)
# # print(len(l))
# my_phone=Phone("Nokia","p9000",89000)
# # print(my_phone) #to avoid  this <__main__.Phone object at 0x00F67160>...use str,rpre
# print(str(my_phone))
# print(repr(my_phone))
# #----------------
# my_phone=Phone("Nokia","p9000",89000)
# my_phone2=Phone("Nokia1223","p900077",890099)
# print(my_phone+my_phone2) #TypeError: unsupported operand type(s) for +: 'Phone' and 'Phone'...use __add__ overloading
#.......................................................................................................
class Phone:
    def __init__(self,brand_name,model,price):
        self.brand_name=brand_name
        self.model=model
        self.price=price
    def phone_name(self):
        return f"{self.brand_name} {self.model}"
    def __len__(self):
         return len(self.phone_name())
class Smartphone(Phone):
    def __init__(self,brand_name,model,price,camera):
        super().__init__(brand_name,model,price)
        self.camera=camera
    def phone_name(self):
        return f"{self.brand_name} {self.model} and {self.price}"
    def __len__(self):
        return self.price
my_phone=Phone("Nokia","p9000",89000)
my_smartphone=Smartphone("oneplus","67gfdgsd",78090,"70mp")
print(my_smartphone.phone_name())
print(len(my_smartphone))
print(len(my_phone))