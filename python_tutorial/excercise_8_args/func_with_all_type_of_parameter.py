#PADK=(parameter,args,default_parameter,kwargs)
#introduction to all type of parameter
# def func(a): #normal parameter
# def func(name='unknown',age=24): #default parameter
#     print(name,age)
# func()
#----------------------------------
#sequence of all 4 parameters
#1)normal parameter
#2)*args
#3)default parameter
#4)**kwargs
def func(name,*args,last_name='unknown',**kwargs): #plz maintain this order
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func('harshit', 1,2,3,4,4,5,6,a=2,b=6,c=8,d = 9)
# func('harshit',1,2,3,a=1,b=2)
#--------------------------
# def func2(name,last_name='unknown'):#1paramater..2default parameter (plz maintain order)
