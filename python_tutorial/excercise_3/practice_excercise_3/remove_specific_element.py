#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']
# def remove_specific_ele(l):
#     un=['Red','Pink', 'Yellow'] #not given position directly given element
#     filter_list=[]
#     for i in l:
#         if i not in un:
#             filter_list.append(i)
#     return filter_list
# word=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# print(remove_specific_ele(word))
#-----------------------
a = [1, 2, 5, 6, 7]
rem = [1, 3]
for i in sorted(rem, reverse=True): 
    del a[i]
print(a)