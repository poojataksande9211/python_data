#A pangram is a unique sentence in which every letter of the alphabet is used at least once. 
import string
string='the quick brown fox jumps over the lazy dog'
def unique(str):
    list2="abcdefghijklmnopqrstuvwxyz"
    for i in list2:
        if i not in str.lower():
            # list2.append(i) #The append() method appends an element to the end of the list.
            return False
        return True
    # if list1==list2:
# string='fox the'
if (unique(string)==True):
    print("pangram")
else:
    print("not pangram")