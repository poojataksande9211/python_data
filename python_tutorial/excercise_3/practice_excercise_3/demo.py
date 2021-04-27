def eve_odd(l):
    even=[]
    odd=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    output=[even,odd]
    return output
num=[1,2,3,4,5,6]
print(eve_odd(num))