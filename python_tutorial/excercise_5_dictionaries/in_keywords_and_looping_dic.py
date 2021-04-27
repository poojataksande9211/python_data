#in keyword and itrations(looping) in dictionaries
user_info={
    'name':'pooja',
    'age':23,
    'fav_movies':['kal ho na ho','raise'],
    'fav_tune':['ha sagari kinara','dis jatil dis yetil'],
}
print(user_info)
#check if key exist in dictionary
# if 'name' in user_info: #in keyword check only for key
#     print("present")
# else:
#     print("not present")
#-----------------------------------
#check if value exist in dictionary
# if 'pooja' in user_info.values():  #values method
#     print("present")
# else:
#     print("not present")
#check if list exist in dic
# if ['kal ho na ho','raise'] in user_info.values():
#     print("present")
# else:
#     print("not present")
#-----------------------------------
#looping
# for i in user_info:
#     print(i) #it will print all key
for i in user_info.values():
    print(i) #it will print all values
for i in user_info: #same as above for loop
    print(user_info[i])
#values method
# user_info_values=user_info.values()
# print(user_info_values)
# print(type(user_info_values))
#-----------------------
#keys method
# user_info_keys=user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))
#-----------------------
#items method
# user_items=user_info.items()
# print(user_items)
# print(type(user_items)) #return o/p in [(),(),(),()] tuple form
for key,value in user_info.items():
    print(f"key is {key} and value is {value}")
for i in user_info.items(): #tuple unpacking print
    print(i)