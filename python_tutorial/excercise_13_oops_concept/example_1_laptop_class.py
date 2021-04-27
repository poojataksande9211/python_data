class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
        self.laptop_name=brand_name+' '+model_name
p1=Laptop("hp","dcp4",50003)
p2=Laptop("intel","cdgb_65_nxx",90000)
# print(p1.brand_name)
# print(p2.brand_name)
print(p2.laptop_name)