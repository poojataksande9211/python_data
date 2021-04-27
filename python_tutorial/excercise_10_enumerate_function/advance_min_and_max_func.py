#advance min and max func
numbers=[1,4,2,8,10]
print(max(numbers))
print(min(numbers))
#-------------------------
def func(item):
    return len(item)
names=['pooja','harshit','vaishishtha','z']
print(max(names,key=func))
print(min(names,key=func))
#--------------------------
#by using lambda function
names=['pooja','harshit','vaishishtha','z']
print(max(names,key=lambda item:len(item)))
#---------------------------------------------
# students2=[
#     {'name':'harshit','score':90,'age':24},
#     {'name':'pooja','score':94,'age':23},
#     {'name':'amit','score':56,'age':14}
# ]
# print(students2)
# # print(max(students2,key=lambda item:item.get('score')))
# print(max(students2,key=lambda item:item.get('score'))['name'])
# print(max(students2,key=lambda item:item.get('age'))['name'])
#--------------------------------------------------
students1= {
    'harshit':{'score':78,'age':24},
    'pooja':{'score':70,'age':64},
    'raja':{'score':98,'age':26},
    'ronitt':{'score':88,'age':44},
}
print(max(students1,key=lambda item:students1[item]['score']))
print(max(students1,key=lambda item:students1[item]['age'])) #according to age