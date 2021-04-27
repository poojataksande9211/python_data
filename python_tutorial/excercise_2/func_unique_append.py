#Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique(list1):
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i) #The append() method appends an element to the end of the list.
    return list2
print(unique([1,2,3,4,4,4,4,5,5,6,5,7,8]))
