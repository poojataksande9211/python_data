def great(a,b):
    if a>b:
        return a
    return b
# print(great(30,40))
def great_new(a,b,c):
    bigger=great(a,b)
    return great(bigger,c)
print(great_new(56,90,22))