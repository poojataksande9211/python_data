#enumerate function
# a=['abc','efg','hijkl'] #without enumerate function
# pos=0
# for i in a:
#     print(f"{pos} {i}")
#     pos=pos+1
#------------------------------------
#with enumerate function
a=['abc','efg','hijkl']
for pos,i in enumerate(a):
    print(f"{pos}---->{i}")
#------------------------------------

