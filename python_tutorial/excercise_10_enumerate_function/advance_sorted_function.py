#advance sorted function
# fruits=['mango','apple','pinaple','banana','peru']  #we can sort only in list
# fruits.sort()#sorted func sort according to alphabet
# print(fruits)
#--------------------------
# #we can't sort in tuple ###error
fruits=('mango','apple','pinaple','banana','peru') 
# fruits.sort()
print(sorted(fruits))
print(fruits)
#------------------------------
# fruits2={'mango','apple','pinaple','banana','peru'}
# print(sorted(fruits2))
#-----------------------------------
guitar=[
    {'model':'yamaha f310','price':8400},
    {'model':'faith naptune','price':6900},
    {'model':'faith apolo venus','price':5400},
    {'model':'tailor 84ce','price':10400}
]
# print(guitar)
print(sorted(guitar,key=lambda item:item.get('price'))) #sorted according to price
# print(sorted(guitar,key=lambda item:item['price']))
# print(sorted(guitar,key=lambda item:item['price'],reverse=True))#sorted reverse list