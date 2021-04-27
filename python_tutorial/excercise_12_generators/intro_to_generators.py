#generators
#generators are iterator##
l=[1,2,3] #iterable ,#we can change iterable to itrator
map(lambda a: a**2,l) #iterator 
# for i in l:
#     print(i)
i=iter(l)
print(next(i)) #we cant directly call to itrable
# print(next(i))
#iterable pe loop chala sakate he(but pahele iter pe call karna padta h)
#iterator pe direct call kar sakta he
#l=[1,2,3,4]
# memory=[.................]#list require maximum memory
# memory=(1)#genrator require min memory,and better performance than list,enerator generator at a time 1 element
# if u want to use sequence no of times then u can use list
# if u want to use sequence at one time then u can use generator