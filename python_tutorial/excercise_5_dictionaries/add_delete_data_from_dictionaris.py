#add and delete data from dictionry
dic={
    'name':'pooja',
    'age':24,
    'last_name':'ganvir',
    'fav_movies':['ram lila','ravan'],
    'fav_tunes':['abhas ha','jar mi paus zale'],
}
print(dic)
dic['fav_song']=['divanagi','jaudyana']  #add data to dic
# print(dic)
#delete data(pop method)
pop_item=dic.pop('fav_tunes') #atleat pass1 argument
print(f"pop item is{pop_item}")
print(dic)
print(type(pop_item))
#----------------------
#popitem method
# pop_it=dic.popitem() #popitem method removes a random item
# print(pop_it)
# print(dic)
# print(type(pop_it))