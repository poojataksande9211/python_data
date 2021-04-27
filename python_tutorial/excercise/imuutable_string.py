#immutable string:=we can not change the origional string
string="sttring"
print(string[1])
# string[1]='T' #(we can not change the character of string it will give an error)
# print(string.replace('t','T')) #(replace method can not change the origional string it will create a new string)
string.replace('t','T')
print(string) #(replace can not chagne origional string)
#.....................
# new_string=string.replace('t','T')
new_string=string.replace('t','T',1)
print(new_string)