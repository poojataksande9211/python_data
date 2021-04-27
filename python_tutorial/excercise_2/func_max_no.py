def max_two(a,b):
    if a>b:
        return a
    return b
def max_three(a,b,c):
    return max_two(c,max_two(a,b))
print(max_three(30,-5,88))