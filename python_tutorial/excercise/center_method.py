name="harshit"
#suppose we want to print *harshit* then use center method
print(name.center(9,"*")) #(we wrote 9 bcz "harshit is a 7 character string +2 star means 9")
print(name.center(11,"*"))
print(name.center(11,"&"))
print(name.center(13,"*"))
name1="she is more beautifull and she is good dancer"
#suppose we dont know the length of the string and we print *string* then 1st find the length
print(len(name1))
print(name1.center(len(name1)+2,"*")) #(we want 2 star hence wrote 2)