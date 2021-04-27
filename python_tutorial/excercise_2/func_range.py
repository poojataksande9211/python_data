#Write a Python function to check whether a number is in a given range
def range_with(n):
    if n in range(3,9):
        print("%s is in the range"%str(n))
    else:
        print("%s is out of the range"%str(n))
range_with(8)