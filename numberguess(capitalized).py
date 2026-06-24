import random

item_list = ['Rock', 'Paper', 'Scissors']
print('                                  ')

print('Welcome to Rock Paper Scissors coded in Python by Humaio!')

print('                                  ')
user_choice = input('''Enter your choice: Rock, Paper, or Scissors? 

Choice: ''')
comp_choice = random.choice(item_list)

#tie statement

print('                                  ') 

if user_choice == comp_choice:

	print(f'Humaio = {comp_choice} & User = {user_choice}')
	print('                                  ')
	print('No one won, the game has tied.')
	print('                                  ')

# rock over scissor

elif user_choice == 'Rock' and comp_choice == 'Scissor' or comp_choice == 'Scissors':

	print(f'Humaio = {comp_choice} & User = {user_choice}')
	print('                                  ')
	print(f'The user has won by selecting {user_choice} over {comp_choice}')
	print('                                  ')

# scissor over rock

elif user_choice == 'Scissor' or user_choice == 'Scissors' and comp_choice == 'Rock':

	print(f'Humaio = {comp_choice} & User = {user_choice}')
	print('                                  ')
	print(f'Humaio has won by selecting {comp_choice} over {user_choice}')
	print('                                  ')

# paper over rock

elif user_choice == 'Paper' and comp_choice == 'Rock':

	print(f'Humaio = {comp_choice} & User = {user_choice}')
	print('                                  ')
	print(f'The user has won by selecting {user_choice} over {comp_choice}')
	print('                                  ')

# rock over paper

elif user_choice == "Rock" and comp_choice == "Paper":

	print(f'Humaio = {comp_choice} & User = {user_choice}')
	print('                                  ')
	print(f'Humaio has won by selcting {comp_choice} over {user_choice}')
	print('                                  ')

# scissor over paper

elif user_choice == "Scissor" or user_choice == 'Scissors' and comp_choice == "Paper":

	print(f'Humaio = {comp_choice} & User = {user_choice}')
	print('                                  ')
	print(f'The user has won by selecting {user_choice} over {comp_choice}')
	print('                                  ')

# paper over scissor

elif user_choice == "Paper" and comp_choice == "scissor" or comp_choice == 'Scissors':

	print(f'Humaio = {comp_choice} & User = {user_choice}')
	print('                                  ')
	print(f'Humaio has won by selecting {comp_choice} over {user_choice}')
	print('                                  ')

else:
	print('                                  ')
	print('Enter correct input.')
	print('                                  ')
	input('Would you like to see the code? y/n')
	if input == 'n':
		print('Thanks for playing!')

	elif input == 'y':
		print('Go to https://'