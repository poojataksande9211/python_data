name,char=input("enter name and single character seperated by comma").split(",")
print(len(name))
# print(f"insensitive count is: {name.lower().count(char.lower())}") #(this will not work during execution time when user enter space after comma)
print(f" insensitive count : {name.strip().lower().count(char.strip().lower())}")
# char.strip().lower()