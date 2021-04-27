#update method in dictionary :=update the dictionary with key and value pair
user_info={
    'name':'pooja ganvir',
    'age':45,
    'last_name':'ganvir',
    'fav_mov':['take off','majali'],
    }
more_info={'state':'maharashtra','dist':['wardha','nagpur']}
user_info.update(more_info)
print(user_info)
#----------------
# more_info={'name':'savita','state':'maharashtra','dist':['wardha','nagpur']}
# user_info.update(more_info) #suppose name is present in dic1 so it will replace the name or update name of dic2 
# print(user_info)
#-----------------------------
# user_info.update({})
# print(user_info)