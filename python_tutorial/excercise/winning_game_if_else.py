#nested if else
winning_num=5
guess_num=input("guess a no")
guess_num=int(guess_num)
if winning_num == guess_num:
    print("u guess no correctly means u win")
elif guess_num < winning_num:
    print("too low")
else:
    print("too high")