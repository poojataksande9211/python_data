#how to check list is empty or not
list1=[1,2,3,456]
if list1:
# if len(list1)>0:
    print("list not empty")
else:
    print("empty")
#------------------------------------
def to_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "u didnt pass any argument"
num=[1,2,3]
print(to_power(3,*num))
# print(to_power(3,*[1,4,5]))