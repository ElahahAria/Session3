import random

while True:

   Roll = input("Enter 'R' to roll the dice :")
   if Roll == 'R':
        Dice = random.randint(1,6)
        if 1 <= Dice <= 5:
            print("The dice shows =" , Dice)
        
        if Dice == 6:
            Bonus_dice_1 = random.randint(1,6)
            Bonus_dice_2 = random.randint(1,6)
            print("Congratulations! You got a lucky 6! , First bonus dice =",Bonus_dice_1 , ", Second bonus dice =",Bonus_dice_2 )
            Break
   
       


    
    
