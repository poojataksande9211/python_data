#count list insight list using type func
def count_list_type(l):
    count=0 
    for i in l:
        if type(i) == list:
            count=count+1
    return count
number=[1,2,3,[1,2],[3,4,5]]
# number=[1,2,3,[4,5,6],"seven",8.0,None]
print(count_list_type(number))