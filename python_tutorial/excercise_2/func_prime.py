#Write a Python function that check the number is prime or not
# num=input("enter no")
# num=int(num)
# for i in range(2,num):
#     if (num%i) ==0:
#         print(num,"not a prime")
#         break
# else:
#     print("prime no")
#.......................................................
num=input("enter no")
num=int(num)
def prime_no(n):
    for i in range(2,num):
        if (num%i ==0):
            print(num,"not prime no")
            break
    else:
        print(num,"is a prime no")
prime_no(num)