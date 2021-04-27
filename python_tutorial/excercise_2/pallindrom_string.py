# # i=0
# name=input("enter name")
# def pallindrom(string):
#     reverse=string[::-1]
#     for i in range(0,len(string)):
#         if reverse[i] == string[i]:
#             return "pallindrom"
#         return "not pallindrome"
# print(pallindrom(name))
#...................................
name=input("enter name")
def pallindrom(string):
    reverse = string[::-1]
    if reverse == string:
        return True
    return False
print(pallindrom(name))