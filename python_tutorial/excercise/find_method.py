#.......find method->use to find out the position of character and word in a string
name="she is more beautiful nd she is good dancer"
print(name.find("is")) #(find the 1st position of is)
print(name.find("is",5)) #(suppose we dont know the 1st and second position of is so find out first position byusing above and then find out second position)
#we want to find the second position of is ande we dont know the 1st position of is....write a program
is_pos1=name.find("is")
is_pos2=name.find("is",is_pos1+1)
print (is_pos2)