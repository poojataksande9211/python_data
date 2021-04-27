#== compare elements of two list (if the elements are same return true otherwise false)
#is compare memory location (if memory locations are same then true otherwise false)
fruits1=["mango","banana","kiwi","pear","pinaple","papaya","apple"]
fruits2=["pear","pinaple","papaya","apple"]
fruits3=["pear","pinaple","papaya","apple"]
print(fruits2==fruits3) #compare elements #return true bcoz elements are same
print(fruits2 is fruits3) #compare memory location (memory loc of fruits2 and fruits3 are diffrent hence return false)