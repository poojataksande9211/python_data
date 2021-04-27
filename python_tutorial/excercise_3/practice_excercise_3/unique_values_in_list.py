#Write a Python program to get unique values from a list.
def unique_value(l):
    uni=[]
    for i in l:
        if i not in uni:
            uni.append(i)
    return uni
num=[1,2,3,4,5,1,2]
word=["a","bc","dc","p","a","bc"]
print(unique_value(num))
print(unique_value(word))
