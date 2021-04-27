#Write a Python function that takes two lists and returns True if they have at least one common member
# def common_no(l1,l2):
#     for i in l1:
#         if i in l2:
#             return "common"
#     return "not common"
# output1,output2=[1,2,3],[1,0,5]
# # output2=[0,2,5]
# print(common_no(output1,output2))
#-------------------------------------
def common_no(l1,l2):
    for i in l1:
        for j in l2:
            if i==j:
                # return "common"
                return True
        # return "not common"
        return False
output1,output2=[1,2,3],[1,0,5]
# output2=[0,2,5]
print(common_no(output1,output2))       