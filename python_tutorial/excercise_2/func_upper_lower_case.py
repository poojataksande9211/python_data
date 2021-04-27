#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# name=input("enter a string")
# upper=0
# lower=0
# for i in name:
#     if i> 'A' and i<='Z':
#         upper=upper + 1
#     elif i> 'a' and i<='z':
#         lower=lower + 1
# # print("uppercase:= "+str(upper))
# # print("lowercase:= "+str(lower))
# print(f"uppercase={upper}")
# print(f"lowercase={lower}")
#......................................
def upper_lower(string):
    upper=0
    lower=0
    for i in string:
        if i>"A" and i< "Z":
            upper=upper+1
        elif i> "a" and i< "z":
        # else:
            lower=lower+1
    print(f"uppercase={upper}")
    print(f"lowercase={lower}")
upper_lower("POOjaganviR")



            
    
