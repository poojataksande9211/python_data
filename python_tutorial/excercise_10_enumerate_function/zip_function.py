#zip function
user_id=['user1','user2','user3']
names=['pooja','amit','raja']
last_name=['ganvir','taksande','sharma']
print(list(zip(user_id,names,last_name)))
# print(dict(zip(user_id,names,last_name))) #error because dict has required only length 2
print(dict(zip(user_id,names)))
#---------------------------------
examples=[('a',1),('b',2)]
print(dict(examples))