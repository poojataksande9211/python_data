#generate list with range function
# number=list(range(1,11))
# print(number)
#----------------------
#something more about pop method
# number=list(range(1,11))
# number.pop() #pop fun delete last element i.e 10
# print(number)
# print(number.pop()) #it will return deleted value -- jab jarurat pade tab use kar sakte h deleted value ko
#----------------------
#index method=>find pertikular element position
# number=list(range(1,11))
number=[1,2,3,4,5,6,7,8,9,10,1]#by default index search from 0th position
print(number.index(1))# find 1element position#
print(number.index(1,2)) #find the 1 last element(2 is used for find 1 after 2nd position)
#----------------------
number=[1,2,3,4,5,6,7,8,9,10,1,7,8,9,10,1]#by default index search from 0th position
print(number.index(1,11)) #find last 1 after 11 position
# print(number.index(1,11,14)) #1 ionfind 1,11 for=start pos to find 1,14=find 1 up to 14 posit

