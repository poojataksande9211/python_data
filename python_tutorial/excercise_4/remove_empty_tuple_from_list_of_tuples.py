def remove_tup(tup):
    tup=filter(None, tup)
    return tup
tup=[([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])]
print(remove_tup(tup))


