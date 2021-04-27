#encapsulation
#abstraction
#in python all are public not private
class Phone:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.__price=price
    def self_call(self,phone_no):
        print(f"calling {phone_no}")
    def full_name(self):
        return f"{self.brand_name} {self.model_name}"
l=[4,2,3,1]
l.sort()#python tym algorithm for sorting
print(l)
#abstraction:- to hide complexity
#naming convention
#_name it means its treated as private variable...convention of private name
#__name__ :-it is called as double underscore//dunder//magic method
phone1=Phone("nokia","1006",10000)
print(phone1._Phone__price)
print(phone1.__dict__)
# phone1._price=-1000
# print(phone1._price)
#name mangaling:use double underscore/tunder
