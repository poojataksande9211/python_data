#program to find pos of string
names=['pooja','harshit','amit','ganvir','aaji']
def find_pos(names,target):
    for pos,i in enumerate(names):
        if i==target:
            return pos
    return -1
print(find_pos(names,'ganvir'))