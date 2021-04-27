# a=int(input("enter first no"))
# b=int(input("enter second no"))
# def great_no(no1,no2):
#     if no1 >no2:
#         return "no1 is grater"
#     else:
#         return "no2 is greater"
# print(great_no(a,b))
#.......................................
a=int(input("enter first no"))
b=int(input("enter second no"))
def great_no(no1,no2):
    if no1 >no2:
        return no1
    return no2
bigger=great_no(a,b)
print(f"{bigger} is greater")