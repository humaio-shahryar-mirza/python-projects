#workflow:

#get input from user(rock, paper or scissors)
#computer choice also shown after input from user
#print result

#CASES:

# 1 - rock
# rock - rock = tie
# rock - paper = paper wins
# rock - scissor = rock wins

# 3 - paper
# paper - paper = tie
# paper - scissor = scissor win
# paper - rock = paper wins

# 3 - scissors
# scissors - scissors = tie
# scissors - rock = rock wins
# scissors - paper = scissors win

import random
item_list = ["rock", "paper", "scissors"]
user_choice = input("enter your move: rock, paper or scissors: ")
computer_choice = random.choice(item_list)


if user_choice == computer_choice:

    print(f"user choice = {user_choice} and computer choice = {computer_choice}")
    print(f"both users have selected the same choice, {user_choice} has been selected by the user and {computer_choice} has been selected by the computer, it is a tie")
    
elif user_choice == "rock" and computer_choice == "paper":
    print(f"user choice = {user_choice} and computer choice = {computer_choice}")
    print(f"the user has selected rock and the computer has selected paper, computer wins")
    
elif user_choice == "paper" and computer_choice == "rock":
    print(f"user choice = {user_choice} and computer choice = {computer_choice}")
    print(f"the user has selected paper and the computer has selected rock, user wins")

elif user_choice == "rock" and computer_choice == "scissors":
    print(f"user choice = {user_choice} and computer choice = {computer_choice}")
    print(f"the user has selected rock and the computer has selected scissors, user wins")

elif user_choice == "scissors" and computer_choice == "rock":
    print(f"user choice = {user_choice} and computer choice = {computer_choice}")
    print(f"the user has selected scissors and the computer has selected rock, computer wins")

elif user_choice == "paper" and computer_choice == "scissors":
    print(f"user choice = {user_choice} and computer choice = {computer_choice}")
    print("the user has selected paper and the computer has selected scissors, computer wins")

elif user_choice == "scissors" and computer_choice == "paper":
    print(f"user choice = {user_choice} and computer choice = {computer_choice}")
    print("the user has selected scissors and the computer has selected paper, user wins")
else:
    print("enter a valid choice next time")