#function_insight_function
# def outer_func():
#     def inner_func():
#         print('insight inner function')
#     return inner_func
# var=outer_func()
# var()
#--------------------------
def outer_func(msg):
    def inner_func():
        print(f"message is:{msg}")
    return inner_func
var=outer_func("hi this is ooonaxcm")
var()