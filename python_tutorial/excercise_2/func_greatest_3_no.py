num1=int(input("enter first no"))
num2=int(input("enter second no"))
num3=int(input("enter third no"))
def great_3_no(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
bigger=great_3_no(num1,num2,num3)
print(f"{bigger} is greater")