def funct(l,**kwargs):
    if kwargs.get('reverse_str')==True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
name=['pooja','amit']
print(funct(name))
print(funct(name,reverse_str=True))