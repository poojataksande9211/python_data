
def fabb(n):
    a=0
    b=1
    print(a,end=" ")
    print(b,end=" ")
    for i in range(2,n-2):
        c=a+b
        a=b
        b=c
    print(b,end=" ") 
fabb(10)