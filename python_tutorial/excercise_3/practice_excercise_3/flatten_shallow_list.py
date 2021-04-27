#Write a Python program to flatten a shallow list.(add all sublist in one list)
def flatten_shallow(l):
    flat=[]
    for sublist in l:
        for i in sublist:
            flat.append(i)
    return flat
# num=[[1,2,3],[4,5,6],[7,8,9]]
num=[[1,-2,-9],[4,5,-8],[7,-7,-9]]
print(flatten_shallow(num))