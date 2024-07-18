#TASK 4: ROCK-PAPER-SCISSORS GAME

import random
l = ["rock","paper","scissor"]

# Initialize the scores outside the while loop
Ccount = 0
Ucount = 0

#to keep the loop running auotmatically
while True:
    uc = int(input('''              
ROCK-PAPER-SCISSORS GAME            
1      Yes        Play
2      No         Exit   
                                                      
                   '''))


#if uc = 1 then game will start(pass) otherwise it will end(break)
    if uc==1:
        for a in range(5):
            userinput = int(input('''

1 Rock
2 Paper
3 Scissor
               ''' ))
            if userinput == 1:
                uchoice = "rock"
            elif userinput == 2:
                uchoice = "paper"
            elif userinput == 3:
                uchoice = "scissor"
            else:
                print("Invalid choice!")
            
#creating the logic of who will win or lose            
            Cchoice = random.choice(l)
#when both choose the same value then it will be a draw
            if Cchoice == uchoice:
                print("Computer Value", Cchoice)
                print("User Value",uchoice)
                print("\nGame Draw Both gets 1 point")
                Ucount = Ucount + 1
                Ccount = Ccount + 1

#on this combinations the user will win and get 1 point 
            elif (uchoice == "rock" and Cchoice == "scissor") or  (uchoice == "paper" and Cchoice == "rock") or (uchoice == "scissor" and Cchoice == "paper"):
                print("Computer Value", Cchoice)
                print("User Value",uchoice)
                print("You Win")  
                Ucount = Ucount + 1

#if that combination is not fullfilled thr computer wins
            else:
                print("Computer Value", Cchoice)
                print("User Value",uchoice)
                print("Computer Win")
                Ccount = Ccount + 1
        
#checking who wins/ loses the game
        if Ucount == Ccount:
            print("Final Game Draw....")
            print("user sccore",Ucount)
            print("computer score", Ccount)

        elif Ucount > Ccount:
            print("user wins...")
            print("user sccore",Ucount)
            print("computer score", Ccount)
        else:
            print("computer wins...")
            print("user sccore",Ucount)
            print("computer score", Ccount)
    
    else:
        break

print("Thanks for playing!")
       



