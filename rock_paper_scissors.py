from random import randint

game = ["rock",'paper','scissor']
comp = game[randint(0,2)]

player = False
count = 0 

while count<3:
    player = input("Choose either rock, paper or scissor : ")
    
    if player == comp:
        print("THe game is a tie")
        
    elif player == "rock": 
        if comp == "paper":
            print("Paper loses to rock")
        else:
            print("Scissor wins")
    elif player == "paper":
        if comp == "scissor":
            print("Scissor beats paper")
        else:
            print("Rock beats paper")   
    elif player == "scissor":
        if comp == "rock":
            print("Rock beats scissor")
        else:
            print("Scissor beats paper")
    else:
        print("Lekhna pani aaudena bhai")
        
    player = False
    comp = game[randint(0,2)]
    count = count + 1