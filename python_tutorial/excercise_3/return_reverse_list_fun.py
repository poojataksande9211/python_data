# def rev_list(l):
#     l.reverse() #reverse string by using reverse method
#     return l
# number=[1,2,3,4,5]
# print(rev_list(number))
#-----------------------------
def rev_list(l):
    return l[::-1] #reverse string by using list slicing
numbers=[1,2,3,4,5]
print(rev_list(numbers))   
#------------------------------
# def rev_string(l):
#     return l[::-1]
# words=["abc","def","ghi"]
# print(rev_string(words))
#-----------------------------
#reverse string by using pop and append method
# def rev_list(l):
#     rev=[]
#     for i in range(len(l)):
#         pop_item=l.pop()
#         rev.append(pop_item)
#     return rev
# numbers=[1,2,3,4,5]
# print(rev_list(numbers))