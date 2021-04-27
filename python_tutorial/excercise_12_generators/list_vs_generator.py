#list_vs_generators
# lsit_1=[ i**2 for i in range(10000000)] #list require maximum memory as compare to generator
# generator_1=(i**2 for i in range(10000000))
#-------------------------------------
#how to calculate time
import time
t1=time.time()
# l=[i**2 for i in range(10000000)] #time required for list is near about 14 sec
g=(i**2 for i in range(10000000)) #time rquired for generator is 0.0 sec
t2=time.time()
print(t2-t1)