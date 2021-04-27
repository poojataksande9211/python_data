class Laptop:
    dis=10
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
        self.laptop_name=brand_name + "" + model_name
    def apply_diss(self):
        off_price=(self.dis/100)*self.price #self likha bcoz use karni he key
        return self.price-off_price
Laptop.dis=10
Laptop1=Laptop("hp","gh234",45000)
Laptop2=Laptop("intell","zoo234",50000)
Laptop2.dis=50
print(Laptop2.apply_diss())
#how to print object variable or namespaces
#to check how many variable present in laptop1
print(Laptop1.__dict__)
