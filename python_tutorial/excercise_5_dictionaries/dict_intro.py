#what are dictionaries:-unordered collections of data in a key: value pair
#how to create dictionaries
# user={"name": "pooja","age" : 23}
# print(user)
# user1={'name':'amit','age':24} #name is a key and value of key is amit
# print(user1)
# print(type(user))
# print(type(user1))
#----------------------------
#second method to create dictionary
user=dict(name='pooja',age=45)
print(user)
print(type(user))
#------------------------------
#how to access data from dictionary(in dic data access by using key,and in list data acccess by using index)
user=dict(name='pooja',age=45)
print(user['name']) #access data by using key value
print(user['age'])
#-------------------------------
#which type of data a dictoinary can store...#anything(number,strings,dictionary,list)
# user_info={
#     'name':'pooja',
#     'age' :34,
#     'fav_movies':['kal ho na ho','raise'],
#     'fav_tunes' :['lag ja gale','aaj he sagai'],
# }
# print(user_info)
# print(user_info['fav_movies']) #fav_movie access by using key
#--------------------------------
#dic within dictionary
# users={
#     'user1' :{
#         'name':'pooja',
#         'age':34,
#         'roll_no':2,
#     },
#     'user2':{
#         'last_name':'ganvir',
#         'house_no' :23,
#         'street_no':4,
#     },
# }
# print(users)
#--------------------------------------
#how to add data to empty dictionary
user_info={}
user_info['name']='pooja'
user_info['age']=45
print(user_info)