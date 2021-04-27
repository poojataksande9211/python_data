#list vs string
#strings are immutable (immutable means u can not change your string)
#we can not add character in string
#list are muttable
s="string"
# s.title() #title method covert 1st charecter of word to uppercase letter
# print(s) #original string cant be change
# p=s.title() #this is new string (u can change in new string)
# print(p) 
l=["word1","word2","word3"]
l.pop()
print(l) #directly change original string
#we add character in list
l.append("word3")
print(l)