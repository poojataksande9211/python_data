#program to multply all the items in list
def mult_list(l):
    total=1
    for i in l:
        total=total*i
    return total
number=[1,2,3,4]
print(mult_list(number))