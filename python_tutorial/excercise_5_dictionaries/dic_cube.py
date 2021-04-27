#write aprogram to return a cube of no using dic
def cube_no(no):
    cube={}
    for i in range(1,no+1):
        cube[i]=i**3
    return cube
print(cube_no(4))