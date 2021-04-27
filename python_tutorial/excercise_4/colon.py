#Write a Python program to create the colon of a tuple.
from copy import deepcopy
mixed=("pooja",1,2,3,[],"amit") #create a tuple
print(mixed)
mixed_colon=deepcopy(mixed) #make copy by using deepcopy func
mixed_colon[4].append(70)
print(mixed_colon)
print(mixed)