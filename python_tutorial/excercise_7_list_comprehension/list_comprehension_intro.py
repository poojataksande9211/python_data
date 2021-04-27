#list comprehension
square=[]
for i in range(1,11):
    square.append(i**2)
print(square)
#by using list comprehension
square2=[i**2 for i in range(1,11)]
print(square2)
#--------------------------
neg=[]
for i in range(1,11):
    neg.append(-i)
print(neg)
negative=[-i for i in range(1,11)]
print(negative)