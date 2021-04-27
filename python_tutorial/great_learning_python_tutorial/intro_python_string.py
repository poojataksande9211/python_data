#intro to python string
#string is a sequence of character enclosed in 'single quote',"double quote",''' triple quote'''
# str1="this is my first string"
# str2='this is my second string'
# str3=''' 
# this string 
# has
# lots of
# lines in it
# '''
# print(str1)
# print(str2)
# print(str3)
#------------------
#extracting individual character in string
my_string="This Is Pooja"
print(my_string)
print(my_string[0])
print(my_string[-1])
print(my_string[5:12])
#string function
print(len(my_string)) #len func
print(my_string.lower()) #lower func
print(my_string.upper()) #upper func
print(my_string)
print(my_string.replace('Is','are'))
abc="apple,banana,apple,dalimba,90,90,90,90,a"
print(abc.count("apple"))
print(abc.count("90"))
print(abc.count("a"))
#----------------------
#find the index 
my_string_1="this is the best example"
print(my_string_1.find("the"))
my_string_2="president obama is the best president of united ststes"
print(my_string_2.split("e"))