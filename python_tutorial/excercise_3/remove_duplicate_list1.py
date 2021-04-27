#program for remove duplicate from list
def duplicate_remove(l):
    lt=[]
    for i in l:
        if i not in lt:
            lt.append(i)
    return lt
num=[10,20,10,30]
print(duplicate_remove(num))