#Write a Python program to print the numbers of a specified list after removing even numbers from it. 
def removing_even(l):
    # common=[]
    for i in l:
        if (i%2==0):
            l.remove(i)
    return l
num=[1,2,3,4,5,6,7,88,100,11,200,211] #output wrong becoz print 100
# num=[11, 22, 33, 44, 55] #output isc orrect 
print(removing_even(num))
#------------------------
