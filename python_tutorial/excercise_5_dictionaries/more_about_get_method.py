#more about get metbod=method return the vaue of item with specified key
user={'name':'pooja','age':34,'age':74}
print(user)#print age 74 bcoz key same hence print last key
print(user.get('name'))
print(user.get('names'))
print(user.get('fav','not found'))
