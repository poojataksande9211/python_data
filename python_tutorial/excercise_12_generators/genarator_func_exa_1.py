# def gen_ex(no):
#     for i in range(1,no+1):
#         if i%2==0:
#             yield(i)
# numbers=list(gen_ex(7))
# for j in numbers:
#     print(j)
#----------------------------------
# def even_gen_ex(no):
#     for i in range(1,no+1):
#         if i%2==0:
#             yield(i)
# numbers=even_gen_ex(8)
# for j in even_gen_ex(8):
#     print(j)
# for j in even_gen_ex(8):
#     print(j)   
#----------------------------------
def gen_ex(no):
    for i in range(2,no+1,2): #skip if i%2==0
            yield(i)
numbers=list(gen_ex(8))
for j in numbers:
    print(j)