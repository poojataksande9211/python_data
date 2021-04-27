#write a program to check list empty or not
def empty_list(l):
     # return type(l)
     for i in l:
          if i in l:
               return "not empty"
     return "empty"     
num=["a"]
print(empty_list(num))
#------------------------------
# def empty_list(l):
#      if len(l)==0:
#           return "empty"
#      return "not empty"
# num=[]     
# print(empty_list(num))
#-----------------------------
# def empty_list(l):
#      if not l:
#           return "empty"
#      return "not empty"      
# num=[]     
# print(empty_list(num))