#decorators_part_2
def decorators_func(any_func):
    def wrapper_fun(*args,**kwargs):
        print("this is awesome function")
        return any_func(*args,**kwargs)
    return wrapper_fun
@decorators_func
def func_1(a):
    print(f"this is function with argument {a}")
func_1(7)
@decorators_func
def add_fun(a,b):
    return a+b
print(add_fun(2,4)) #it will not print output...print none ....change return any_func