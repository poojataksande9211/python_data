#dictionary_comprehension
# square={1:1,2:4,3:9}
square1={num:num**2 for num in range(1,4)}
print(square1)
#-----------------------
square1={f"square of {num} is":num**2 for num in range(1,4)}
for k,v in square1.items():
    print(f" {k}:{v}")
# print(square1)
#--------------------------
string="harshit"
dic_count={char:string.count(char) for char in string}
print(dic_count)