#write a program to get largest no from list
# def largest_no(l):
#     return max(l)
# number=[1,4,90,67]
# print(largest_no(number))
#--------------------------
def largest_no(l):
    great=l[0]
    for i in l:
        if i>great:
            great=i
    return great
    
number=[1,4,90,1020]
print(largest_no(number))  
