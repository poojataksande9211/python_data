#print seperated output in dic by user input
user={}
name=input("enter your name:") 
age=input("enter your age:")
fav_movies=input("enter your fav movies seperated by comma:").split(",")
fav_songs=input("enter your fav songs seperated by comma:").split(",")
user['name']=name
user['age']=age
user['fav_movies']=fav_movies
user['fav_songs']=fav_songs
# print(user)
for key,value in user.items():
    print(f"{key}:{value}")