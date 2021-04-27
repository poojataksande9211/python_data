num=input("enter number")
i=0
total=0
# while i < int(num[-1]): #(-1 means last digit of string)
while i < len(num):
    total=total + int(num[i])
    i=i+1
print(total)