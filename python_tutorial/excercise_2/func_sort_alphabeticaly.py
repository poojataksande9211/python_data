#Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically
# item=input("enter input seperated by minus").split("-")
# # item.sort()
# for i in item:
#     item.sort()
# print('-'.join(item))
#....................................................
item=input("enter input seperated by minus").split("-")
def sort_alphabet():
    for i in item:
        item.sort()
# print('-'.join(item))
sort_alphabet()
print('-'.join(item))