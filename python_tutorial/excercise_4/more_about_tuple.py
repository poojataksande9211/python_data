#looping in tuples
mixed=(1,2,3,4,5,6,4.0)
# for i in mixed:
#     print(i)
# i=0
# while i<len(mixed):
#     print(mixed[i])
#     i=i+1
#-------------------------
#tuple with one element
# mixed=(1,2,3,4,5,6,4.0)
# print(type(mixed)) #shows tuple
# num=(1)
# word=("word")
# print(type(num)) #shows int type not tuple
# print(type(word)) #shows string type not tuple
# num1=(1,)
# print(type(num1))
#------------------------------------------
#tuple without paranthesis
# fruits="banana","mosambi","apple","pinaple"
# print(type(fruits))
# num=1,2,3,4,5
# print(type(num))
#------------------------------------------
#tuple unpacking
# gitarist=("maneli jamal","ediee van re deer","andrew fay")
# gitarist1,gitarist2,gitarist3=gitarist
# print(gitarist1)
#---------------------------------------------
#list insight tuples
# favoriets=("southern mangolia",["tokiyo gokul theme","landscape"])
# favoriets[1].pop()
# print(favoriets)
# favoriets[1].append("we made it")
# print(favoriets)
#-------------------------------------------
#func used in tuples
num=(1,2,3,4,5,6,4.5)
print(min(num))
print(max(num))
print(sum(num))