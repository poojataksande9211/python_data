#Write a Python function to check whether a number is perfect or not
#If the sum of the proper divisors of the number is equal to the original number, the number is a Perfect number.
# no=28
# sum=0
# for i in range(1,no):
#     if (no%i == 0):
#         sum=sum+i
# if sum==no:
#     print(no,"is perfect no")
# else:
#     print(no," is not perfect no")
#..................................
def perfect_no(no):
    sum=0
    for i in range(1,no):
        if (no%i ==0):
            sum=sum+i
    if sum==no:
        print(no,"is perfect no")
    else:
        print(no,"is not perfect no")
perfect_no(6)
    