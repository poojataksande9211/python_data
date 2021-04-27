#write first generator with generator function
#generator can form by using two fun
#1.generator func
#2.generator comprehension
def nums(n):
    for i in range(1,n+1):
        yield(i)
# print(nums(10))
numbers=list(nums(10))
for num in numbers:
    print(num)
# for num in numbers:
#     print(num)