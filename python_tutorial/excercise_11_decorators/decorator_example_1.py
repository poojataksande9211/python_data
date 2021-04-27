from functools import wraps
import time
def calculate_time(any_func):
    @wraps(any_func)
    def wraper_func(*args,**kwargs):
        print(f"Executing.....{any_func.__name__}")
        t1=time.time()
        return_value=any_func(*args,**kwargs)
        t2=time.time()
        total_time=t2-t1
        print(f"this func took {total_time} seconds")
        return return_value
    return wraper_func
@calculate_time
def square_finder(n):
    return[i**2 for i in range(1,n+1)]
square_finder(10000)