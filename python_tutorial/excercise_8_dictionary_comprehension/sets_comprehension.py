#sets comprehension
ss={k**2 for k in range(1,11)} #no need to write key
print(ss)
#----------------------
names=['pooja','harshit','hsssg','goo']
first={name[0] for name in names}
print(first)