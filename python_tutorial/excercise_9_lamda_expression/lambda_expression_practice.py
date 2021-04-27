# def is_even(a):
#     if a % 2 ==0:
#         return True
#     return False
#orrrrr
def is_even(a):
    return a%2 ==0
print(is_even(4))
#--------------------------
is_even_2=lambda a:a%2==0
print(is_even_2(5))
#--------------------------
# def last_char(s):
#     return s[-1]
# print(last_char('pooja'))
last_char2=lambda s:s[-1]
print(last_char2('pooja'))
#------------------------------
#lambda with if else
# def func(s):
#     if len(s)>5:
#         return True
#     return False
# print(func('pooja'))
#orrrrrr
def func(s): #above shortcut
    return len(s)>5
print(func('pooja'))
#--------------------------
# func2=lambda s: len(s)>5 #without if else
# print(func2('poojas'))p
func2=lambda s:True if len(s)>5 else False
print(func2('poojas'))

