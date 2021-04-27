#property and setter decoration
class Phone:
    def __init__(self,model_name,brand,price):
        self.model_name=model_name
        self.brand=brand
        self._price=max(price,0)
        # if price > 0:
        #     self._price= price
        # else:
        #     self._price=0
        # self.complete_specification=f"{self.model_name} {self.brand} and price {price}"
    @property
    def complete_specification(self):
        return f"{self.model_name} {self.brand} and price {self._price}"
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        self._price=max(new_price,0)
    def make_a_call(self,phone_no):
        print(f"calling {phone_no}.......")
    def full_name(self):
        return f"{self.model_name} {self.brand}"
p1=Phone("nokia","67ffg",-5000) #suppose user enter -ve value to avoid this
p1.make_a_call(9595136724)
print(p1.model_name)
print(p1.brand)
# p1._price=-500
# print(p1._price) #without settur
print(p1._price) #with setter 
# print(p1.complete_specification()) #without property use as function 
print(p1.complete_specification) #with property decorators use as without paranthesis 