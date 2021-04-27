#SUMMURY
def add(a,b):
    return a+b
print(add(3,4))
#-------------------------
def add_args(*args): #args gather as tuple
    total=0
    for num in args:
        total=total+num
    return total
# print(add_args(1,2,3,4,5))
l=[1,2,3]
print(add_args(*l)) #to adds list unpack list using (*)
#---------------------------------------
#kwargs=keyword argument, **
def fun(**kwargs):
    print(kwargs) #kwargs gather as dictionary
    print(type(kwargs))
fun(name='harshit',age=24)
#-------------------------------------------
#args,kwargs,normal parameter,default parameter
#PADK(parameter,args,default parameter,kwargs)
def fun2(name,*args,last_name='unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
print(fun2('pooja',1,2,3,4,a=2,b=4,f=7))