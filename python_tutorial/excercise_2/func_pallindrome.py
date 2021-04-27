#Write a Python function that checks whether a passed string is palindrome or not
#A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam
# string="navan"
# for i in string:
#     reverse=string[::-1]
# if reverse==string:
#     print(string,"is pallindrome")
# else:
#     print(string,"is not pallindrome")
def pallindrome(string):
    for i in string:
        reverse=string[::-1]
    if reverse==string:
        print(string,"is pallindrome")
    else:
        print(string,"is not pallindrome")
pallindrome("madam")