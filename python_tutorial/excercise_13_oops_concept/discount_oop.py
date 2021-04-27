class Laptop:
    def __init__(self,brand_name,model,price):
        self.brand_name=brand_name
        self.model=model
        self.price=price
    def apply_diss(self,dis_num):
        off_price=(dis_num/100) *self.price
        return self.price-off_price

Laptop1=Laptop("hp","gf45",50000)
print(Laptop1.apply_diss(10))
        