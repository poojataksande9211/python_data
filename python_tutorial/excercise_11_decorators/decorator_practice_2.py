#decorator_practice_2
from functools import wraps
def only_int_allow(any_func):
    @wraps(any_func)
    def wraper_func(*args,**kwargs):
        if all ([type(i)==int for i in args]): #represent all commented code in ane line
            return any_func(*args,**kwargs)
        print("invalid argument")
        # data_type=[]
        # for i in args:
        #     data_type.append(type(i)==int)
        # if all(data_type):
        #     return any_func(*args,**kwargs)
        # else:
        #     print("invalid argument")
    return wraper_func

@only_int_allow
def add_all(*args): 
    total=0
    for i in args:
        total=total+i
    return total
# print(add_all(1,2,3,4,5,6,[1,2,3]))
print(add_all(1,2,3,4,5,6))