#decorators intro(inhance the functionality of other function)
#decorators is a function which increse the functionality of other function
# def decorator_function(any_func):
#     def wraper_func():
#         print("this is awesome function")
#         any_func()
#     return wraper_func
# def func1():
#     print("this is function1")
# def func2():
#     print("this is function 2")
# var=decorator_function(func2)
# var()
#---------------------------------------
#@ symbol use for the decorators
def decorator_function(any_func):
    def wraper_func():
        print("this is awesome function")
        any_func()
    return wraper_func
@decorator_function #this is shortcut
def func1():
    print("this is function1")
func1()
@decorator_function
def func2():
    print("this is function 2")
func2()