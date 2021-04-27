#Write a Python program to find the second smallest number in a list
def second_smallest_no(l):
    length=len(l)
    l.sort() #sort method sort the link ascending by default
    print("largest no is:-",l[length-1])
    print("second largest no is:-",l[length-2])
    print("smallest no is:-",l[0])
    print("second smallest no is:-",l[1])
num=[10,20,4,89,70,3,2,1]
second_smallest_no(num)
