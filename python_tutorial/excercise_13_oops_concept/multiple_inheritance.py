#multiple inheritance 
class A:
    def class_a_method(self): #instance method
        return "I'm just a class A method"
    def hello(self): #instance method
        return "hello from class A"
class B:
    def class_b_method(self):
        return "I'm just class B method"
    def hello(self):                   #to Execute class B hello method to change order of class C(B,A) 
        return "hello from class B "
class C(A,B):
    pass
instance_c=C() #instance /object
# print(instance_c.class_a_method())
# print(instance_c.class_b_method())
# print(instance_c.hello()) #it print hello from class A not from b....seee mro of class c
# print(help(C))#to check mro
# print(C.mro())#to check mro
print(C.__mro__) #to check mro
