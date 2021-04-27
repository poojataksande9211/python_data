#args_as_argument
def multiply(*args):
    multi=1 #([1,2,3,4])
    print(args)
    for i in args:
        multi *=i
    return multi
num=[1,2,3,4]
# num=(1,2,3,4) #you can use tuple instead of list
print(multiply(*num)) # * use for unpack