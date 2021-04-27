# win_num=45
import random
win_num=random.randint(1,100)
guess=1
guess_num=input("enter a no between 1 to 100")
guess_num=int(guess_num)
game_over=False
while not game_over:
    if guess_num == win_num:
        print(f"YOU WIN,and you guess a no in {guess} times")
        game_over=True
        
    else:
        if guess_num <win_num:
            print("TOO LOW")
            
        else: 
            print("TOO HHIG")
        guess=guess+1
        guess_num=int(input("AGAIN enter no")) #(no need to write both the statement in if else block )
