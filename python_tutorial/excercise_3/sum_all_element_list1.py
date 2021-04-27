#write a python program to sum all the item in list
def sum_all_element(l):
    total=0
    for i in l:
        total=total+i
    return total
numbers=[1,2,3,4,5]
print(sum_all_element(numbers))