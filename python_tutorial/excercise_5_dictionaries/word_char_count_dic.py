#word counter
def char_count(s):
    count={}
    for i in s:
        count[i]=s.count(i)
    return count
print(char_count('pooja'))