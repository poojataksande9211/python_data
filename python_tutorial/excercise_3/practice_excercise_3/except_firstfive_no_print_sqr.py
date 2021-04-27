#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30
def square_exclude_first_five():
    lic=[]
    for i in range(1,21):
        lic.append(i**2)
    print(lic[5:])
# num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
square_exclude_first_five()