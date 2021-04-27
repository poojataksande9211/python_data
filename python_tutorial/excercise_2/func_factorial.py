num=int(input("enter no"))
def factorial(no):
    fact=1
    if no <0:
        print("-ve no factorial not exist")
    else:
        for i in range(1,no+1):
            fact=fact*i
        return fact
print(factorial(num))