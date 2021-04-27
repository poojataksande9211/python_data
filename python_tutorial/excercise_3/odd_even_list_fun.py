#filter odd even...define function...input list [1,2,3,4,5,6]...[[2, 4, 6], [1, 3, 5]]
def odd_even(l):
    even_list=[]
    odd_list=[]
    for i in l:
        if (i%2)==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    output=[even_list,odd_list]
    return output
number=[1,2,3,4,5,6]
print(odd_even(number))