#convert a integer to string 
def num(l): #without comprehension
    new_list=[]
    for i in l:
        if type(i)==int or type(i)==float:
            new_list.append(str(i))
    print(new_list)
num([True,False,[1,2,4],6,7,1.0])

# def num(l): #with comprehension
#     return [str(i) for i in l if (type(i)==int or type(i)==float)]
# print(num([True,False,[1,2,4],6,7,1.0]))