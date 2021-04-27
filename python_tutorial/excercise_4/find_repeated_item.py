# Write a Python program to find the repeated items of a tuple.
# mixed=(1,2,3,3,2,4,5,6)
# print(mixed)
# count=mixed.count(3)
# print(f"repeated item of 3 is::{count}")
#-----------------------------------------------
mixed=(1,2,3,3,2,4,5,6)
for i in mixed:
    if mixed.count(i)>1:
        print(i,"repeated")
    else:
        print(i,"not repeated")