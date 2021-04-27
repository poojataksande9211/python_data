#dcorator with argument
from functools import wraps
def only_data_type_allowe(data_type):
    def decorator(func):
        @wraps(func)
        def wraper_func(*args,**kwargs):
            if all([type(arg==data_type for arg in args)]):
                return func(*args,**kwargs)
            print("invalid argument")
        return wraper_func
    return decorator

@only_data_type_allowe(str)
def string_join(*args):
    string=""
    for i in args:
        string+=i
    return string
print(string_join("harshit","vaishisht"))