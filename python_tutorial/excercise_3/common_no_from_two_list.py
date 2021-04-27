#commen element finder function...take 2 list as input...output common element of both list..[1,2,3],[1,2,4]....[1, 2]
def common_filter(l1,l2):
    comman=[]
    for i in l1:
    # for i in range(len(l1)):
        if i in l2:
            comman.append(i)
    return comman
number1,number2=[1,2,3],[1,2,4]
print(common_filter(number1,number2))
# print(common_filter([1,2,3],[1,2,4]))