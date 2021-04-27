#Write a Python function to multiply all the numbers in a list. Go to the editor Sample List : (8, 2, 3, -1, 7)
def multiply(numbers):
    multy=1
    for i in numbers:
        multy=multy*i
    return multy
print(multiply((8,2,3,-1,7)))