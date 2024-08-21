from art import logo
import random
import os


# ~ Unnecessary function declaration to get a random number ;-)
def get_random_number():
	return random.randint(1, 100)

	
game_over = False

while not game_over:
	os.system('cls' if os.system == 'nt' else 'clear')
	print(logo)

	print("Welcome to the Number Guessing Game")
	print("I'm thinking of a number between 1 and 100. \nYou have to guess the number I'm thinking...")
	level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

	if level == 'easy':
		tries = 10
	elif level == 'hard':
		tries = 5
	else:
		print('Wrong input. Exiting...')

	random_number = get_random_number()
	while tries > 0:
		print(f"  You have {tries} attempts to guess the number.")
		guess = int(input("   Make a guess: "))
		if guess < random_number:
			print("    Too low")
		elif guess > random_number:
			print("    Too high")
		else:
			print(f"    You are correct. The number that I guessed is {random_number}")
			tries = 0
		tries -= 1
	
	if tries == 0:
		print("\n   Sorry. You have lost.")
	user_input = input("\nDo you want to play another game? Y or N: ").lower()
	
	if user_input == 'n':
		game_over = True
