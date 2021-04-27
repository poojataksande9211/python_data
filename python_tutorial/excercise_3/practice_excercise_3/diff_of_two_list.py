#Write a Python program to get the difference between the two lists.
#a=[1,2,3,4,5]
#b=[1,5,6,7,8,9]
a=[1, 3, 5, 7, 9]
b=[1, 2, 4, 6, 7, 8]
diff_a_b=list(set(a)-set(b))
diff_b_a=list(set(b)-set(a))
total_diff=diff_a_b + diff_b_a
print(total_diff)