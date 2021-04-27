#find average
#[1,2,3],[4,5,6],[7,8,9]
# def average_finder(l1,l2): #this is only for 2 list
#     average=[]
#     for pair in zip(l1,l2):
#         average.append(sum(pair)/len(pair))
#     return average
# print(average_finder([1,2,3],[4,5,6]))
#-----------------------------------
#find avg of n number of list
def average_finder(*args): #this is only for 2 list
    average=[]
    for pair in zip(*args): #*args use for unpacking purpose...args=([],[])
        average.append(sum(pair)/len(pair))
    return average
print(average_finder([1,2,3],[4,5,6],[7,8,9]))
#--------------------------------------------
#find avg using single line
# def average_finder(*args):
average_fin=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
print(average_fin([1,2,3],[4,5,6],[7,8,9]))