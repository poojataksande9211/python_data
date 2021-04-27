#Write a Python program to find the list of words that are longer than n from a given list of words
# def len_longer(n,l):
#     longer=[]
#     for i in l:
#         if len(i)> n:
#           longer.append(i)
#     return longer
# num=["pooja","amit","vivek","banduji","abc","def"]
# print(len_longer(5,num))
#-------------------------------
def len_longer(n,str):
    longer=[]
    txt=str.split(" ")
    for i in txt:
        if len(i)> n:
          longer.append(i)
    return longer
print(len_longer(3,"this is pooja amit ganvir"))