def fabb(no):
    a=0
    b=1
    total=0
    print(a,end=" ")
    print(b,end=" ")
    for i in range(0,no+1):
        total=a+b
        a=b
        b=total 
        print(b,end=" ")
fabb(10)