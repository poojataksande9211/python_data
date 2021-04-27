#more about python
s={1,2,3,4,5,6}
#check if item present in set or not
if 1 in s:
    print("present")
else:
    print("not present")
#-----------------------
for i in s:
    print(i)
#---------------------
#remove duplicate data from tuple
sa=(1,2,3,2,4,5)
print(type(sa))
sa=set(sa)
print(sa)
#---------------------
#set math
s2={1,2,3,4}
s3={2,3,7,8}
#union
s2_s3_union=s2 |s3
print(s2_s3_union)
#intersection #count common value
s2_s3_intersection=s2 & s3
print(s2_s3_intersection)