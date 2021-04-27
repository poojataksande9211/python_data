#Write a Python program to count the number of elements in a list within a specified range.
def count_specified_range(l,s,e):
    t=0
    for i in l:
        if i>=s and i<=e:
            t=t+1
    return t
num=[2,4,5,7,8,9,10,20,30,40,60]
s=8
e=60
print(count_specified_range(num,s,e))