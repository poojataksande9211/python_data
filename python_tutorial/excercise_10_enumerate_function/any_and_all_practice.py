#any a nd all practice
def total_sum(*args):
    if all([type(arg)==int or type(arg)==float for arg in args]):
        total=0
        for num in args:
            total+=num
        return total
    else:
        return "wrong input"
# print(total_sum(1,2,3,4,5.0,'harshit',['pooja']))
print(total_sum(1,2,3,4,5.0))
