#program for count 1st and last character same in list
def count_char_same(l):
    t=0
    for i in l:
        if i[0]==i[-1]:
            t=t+1
    return t
words=["poja","aba","abca","jaban","poop"]
print(count_char_same(words))

