#filter function
# def is_even(a):
#     return a%2==0
# numbers=[1,2,3,4,5,6,7,8,9]
# evens=tuple(filter(is_even,numbers))
# print(evens)
#---------------------
#by using lambda expression
# def is_even(a):
#     return a%2==0
# numbers=[1,2,3,4,5,6,7,8,9]
# evens=tuple(filter(lambda a:a%2==0,numbers)) 
# print(evens)
#--------------------------
#by using list comprehension
numbers=[1,2,3,4,5,6,7,8,9]
new_even=[i for i in numbers if i%2==0]
print(new_even)
#-------------------------------