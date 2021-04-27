#if elif else used when we want to check multiple conditions
age=input("enter your age :")
age=int(age)
if age <=1:
    print ("u cant watch movie")
elif age >1 and age <=3:
    print (" ticket is free")
# elif age >3 and age <= 10:
# elif age >3<=10:
elif 3<age<=10:
    print("ticket price is 150")
elif age >10 and age <=60:
    print("ticket price is 250")
else:
    print("ticket price is 300")
