from random import choice

from hangman_art import hangman_logo, hangman_stages
from hangman_words import word_list

def start_game():
	print(hangman_logo)
	
	chosen_word = choice(word_list)

	display = []
	lives = 6

	for letter in chosen_word:
		if letter == " ":
			display.append(" ")
		else:
			display.append("_")

	print(hangman_stages[lives] + "\n")
	print(" ".join(display))

	end_of_game = False
	
	while not end_of_game:
		user_guess = input("\nGuess a letter: ").lower()

		if user_guess not in chosen_word:
			lives -= 1
			if lives != 0:
				print(f"\nYou have {lives} chances left.")

		for i in range(len(chosen_word)):
			if chosen_word[i] == user_guess:
				display[i] = user_guess

		print("\n" + hangman_stages[lives] + "\n")	
		print(" ".join(display))
		
		if "_" not in display:
			end_of_game = True
			print("\nCongrats. You won.")
			confirm_restart()
		
		if lives == 0:
			print("\nSorry. You lost.")
			print(f"\nThe word was {chosen_word}")
			end_of_game = True
			confirm_restart()

def confirm_restart():
	replay_input = input("\nDo you want to play another round? Y or N? ").lower()
	if replay_input == 'y':
		start_game()

start_game()


