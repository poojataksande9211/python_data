#dictionary is an unorder collection of key-value pair enclosed with {}
#dictinary is muttable
d1={"apple":50,"banana":40,"guava":70,"pinaple":56}
print(d1)
#how to extact individual element from dic
print(d1.keys())
print(d1.values())
#------------------
#how to addd new element in dict
d1['wtermelon']=90
print(d1)
#how to modify existing element
d1["apple"]=100
print(d1)
#----------------------
#dictionary function
#update 
d2={"muskmelon":96,"papaya":45}
d1.update(d2)
print(d1)
#pop:remove element
print(d1.pop("guava"))
print(d1)