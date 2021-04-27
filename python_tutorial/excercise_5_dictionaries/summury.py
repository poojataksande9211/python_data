#dictionry summury
# d={'name':'pooja','age':23}#name and age are key....pooja and 24 are value
# print(d)#there is no indexing in dictionary
# d1=dict(name='harshit',age=23) 
# print(d1)
d3={
    'name':'pooja',
    'age':23,
    'fav_mov':['ddlj','fun'],
    'fav_song':['tu hi re','angat mazi ya'],
    }
print(d3)
#how to access data from dic
print(d3['name'])
# print(d1['age'])
#add data to empty dic
# empty_dic={}
# empty_dic['key1']='value2'
# empty_dic['key2']='value2'
# print(empty_dic)
#check key present in dic using in
# if 'names' in d3:
#     print("present")
# else:
#     print("not present")
#how to iterated over dictionary
for key,value in d3.items():
    print(f"{key} and {value}")
#print all keys
# for i in d3:
#     print(i)
#to print all values
# for i in d3.values():
#     print(i)
#most common method in dict(get method)
# print(d3['name'])
# print(d3.get('name'))#method is used to acces key it returns none when key is not present in dic
# print(d3.get('names'))
#to delete item
#pop ....take 1 argument which is key name
# popped=d3.pop('name')
# print(popped)
# print(d3)
#popitem...it delete randomely items
popped_item=d3.popitem()
print(popped_item)
print(d3)