#iterator vs iterable
# numbers=[1,2,3,4,5] #tuple,string are iterables
# squars=map(lambda a:a**2,numbers) #iterator
# print(squars) #it returns map object,map object pe loop chala sakte he
# # for i in numbers:
# for i in squars:
#     print(i)
#---------------------------------
#how to execute for loop
#first call iter function
#second call next function
numberss=[1,2,3,4,5]
num_iter=iter(numberss)
print(next(num_iter)) #output 1
print(next(num_iter)) #output 2
print(next(num_iter)) 
print(next(num_iter)) 
print(next(num_iter)) 
# print(next(num_iter))  #output stop iteration
# print(next(numberss)) #numberss is not an iterator