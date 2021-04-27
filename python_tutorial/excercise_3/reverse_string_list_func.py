def rev_string(l):
    element=[]
    for subelement in l:
        element.append(subelement[::-1])
    return element

words=["abc","def","ghi"]
print(rev_string(words))
#----------------------------
# def rev_string(l):
#     element=[]
#     for subelement in range(len(l)):
#         element.append(subelement[::-1])  #why error for i in l ///for i in range(len(l))
#     return element

# words=["abc","def","ghi"]
# print(rev_string(words))
#----------------------------                                                                            
# words=["abc","def","ghi"]
# for i in words:
#     print(i)
#----------------------------
# def rev_string(l):
#     rev=[]
#     for i in range(len(l)):
#         pop_item=l.pop()
#         rev.append(pop_item)
#     return rev
# words=["abc","def","ghi"]
# print(rev_string(words))