import random

user_wins = 0
computer_wins = 0
game_ties = 0

options=["rock","paper","scissors"]
#options[0] #choosing just one element in the list

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input =="q":
        break

    if user_input not in options:
        continue #re-asks them

    random_number =  random.randint(0,2)
    # Rock = 0, paper = 1, scissors = 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print('You won!')
        user_wins += 1
        

    elif user_input == "paper" and computer_pick == "rock":
        print('You won!')
        user_wins += 1
        

    elif user_input == "scissors" and computer_pick == "paper":
        print('You won!')
        user_wins += 1

    elif user_input == "rock" and computer_pick == "rock":
        print('You Tied!')
        game_ties += 1

    elif user_input == "paper" and computer_pick == "paper":
        print('You Tied!')
        game_ties +=1

    elif user_input == "scissors" and computer_pick == "scissors":
        print('You Tied!')
        game_ties += 1
    
    else:
        print("You lost!")
        computer_wins += 1
        
print("You Tied ",game_ties, ' times')
print("You won ",user_wins, ' times')
print("Computer won ", computer_wins, " times")
print("Nice one! Goodbye!") #had to write in all code for Tieing, dude didnt show that only win/loose