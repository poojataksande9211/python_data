#kwargs/keyword argument/double star operator
# def func(**kwargs): #*args gather argument in to tuple
#     print(kwargs)   #**kwargs gather argument in dictionary
#     for k,v in kwargs.items():
#         print(f"{k} : {v}")
# func(first_name='harshit',last_name='vaishista')
#-------------------------------
# def func(name,**kwargs): #*args gather argument in to tuple
#     print(kwargs)   #**kwargs gather argument in dictionary
#     for k,v in kwargs.items():
#         print(f"{k} : {v}")
# func('pooja',first_name='harshit',last_name='vaishista')
#-------------------------------
#dictionary unpacking
def func(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(f"{k} : {v}") 
dd={'name':'pooja','age':24}
func(**dd)