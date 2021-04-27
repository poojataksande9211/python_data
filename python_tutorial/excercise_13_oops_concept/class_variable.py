# class Circle():
#     def __init__(self,radius,pi):
#         self.radius=radius
#         self.pi=pi
#     def cal_circumference(self):
#         return 2*self.pi*self.radius
# c=Circle(4,3.14)
# c1=Circle(5,3.14)
# print(c.cal_circumference())
#-------------------------------------
#by using class variable
# class Circle():
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def cal_circumference(self):
#         return 2*Circle.pi*self.radius
# c=Circle(4)#pi value use no of times hence use class variale
# c1=Circle(5)
# print(c.cal_circumference())
#-----------------------------------
#10% discount on all product
class Laptop:
    dis=10
    def __init__(self,brand_name,model_name,price):
        #instance variable
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
        self.laptop_name=brand_name + '' +model_name
    def apply_diss(self):
        off_price=(Laptop.dis/100)*self.price
        return self.price -off_price

laptop1= Laptop("hp","jhf22",30000)
laptop2= Laptop("intel","rjs33",60000)
print(laptop1.apply_diss())