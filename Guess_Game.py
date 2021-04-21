#Guess Game

from random import randint
while input("DO YOU WANT TO PLAY VERY INTERESTING GUESS GAME!!(YES/NO)").strip().lower() == 'yes':
    com_guess = randint(1,50)
    chance = 5
    while chance > 0:  
        print(f"\n\n You Have {chance} Left!!")
        user_guess = int(input("Please Enter your Guess"))
        if user_guess > 50 or user_guess < 1:
            print("\n\n!!!!WARNING!!! Please Enter (1-50)only")
            continue
        if user_guess == com_guess:
            print("\n\n!!!YOU ARE SUCH A MASTER!!!!")
            break
        elif user_guess > com_guess:
            print("\n\n!!HINT: Please think some low value!!")
        else:
            print("\n\n!!HINT: Please think some High value!!")
        chance -=1    
    else:
        print(f"\n\n!!Computer Guess was {com_guess}!!")
        print("\n\n!!ha ha ha!! You such a Looser!!!")
        print("\n\n")             
                 
                            
             
                       
             
             
 
