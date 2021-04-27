#decoratos_part_3
from functools import wraps
def decorator_func(any_func):
    @wraps(any_func)
    def wrapper_func(*args,**kwargs):
        "this is wrapper func"
        print("this is awesome func")
        return any_func(*args,**kwargs)
    return wrapper_func
@decorator_func
def add(a,b):
    "this is add func"
    return a+b
print(add.__doc__) #without function tool import wrap it cant be possible
print(add.__name__)