#decorators_practice
from functools import wraps
def print_data_decorators(any_func):
    @wraps(any_func)
    def wraper_func(*args,**kwargs):
        print(f"you are calling {any_func.__name__}")
        print(f"{any_func.__doc__}")
        return any_func(*args,**kwargs)
    return wraper_func
    
@print_data_decorators
def add(a,b):
    """"this function takes 3 numbers as argument and return their sum"""
    return a+b
print(add(5,5))