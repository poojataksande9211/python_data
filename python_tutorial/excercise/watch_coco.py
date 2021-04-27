user_name=input("enter your name?")
user_age=input("enter your age?")
user_age=int(user_age)
if (user_name[0] == "a" or user_name[0] == "A") and user_age >=10:
    print("u can watch movie")
else:
    print("sorry u cant watch movie")