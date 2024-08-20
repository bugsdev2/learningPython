from blackjack_art import logo
import random
import os




def deal_card():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	return random.choice(cards)
	
	
def get_total(cards):
	if sum(cards) == 21 and len(cards) == 2:
		return 0
	if 11 in cards and sum(cards) > 21:
		cards.remove(11)
		cards.append(1)
		
	return sum(cards)
	
	
def compare(user_score, computer_score):
	if user_score == computer_score:
		return "\nDraw"
	elif computer_score == 0:
		return "\nYou Lose. Computer has Blackjack."
	elif user_score == 0:
		return "\nYou win with a Blackjack."
	elif user_score > 21:
		return "\nYou went over 21. You lose."
	elif computer_score > 21:
		return "\nComputer went over 21. You win"
	elif user_score > computer_score:
		return "\nYou win." 
	else: 
		return "\nYou lose."
		

def play_game():
	os.system('cls' if os.name == "nt" else 'clear')
	print(logo)
	user_cards = []
	computer_cards = []
	is_game_over = False

	for i in range(2):
		user_cards.append(deal_card())
		computer_cards.append(deal_card())



	while not is_game_over:
		user_score = get_total(user_cards)
		computer_score = get_total(computer_cards)

		print(f"\nYour cards: {user_cards}, current score: {user_score}")
		print(f"\nConputer's first card: {computer_cards[0]}")

		if user_score == 0 or computer_score == 0 or user_score > 21:
			is_game_over = True
		else:
			user_input = input("\nDo you want to draw another card? Y for Yes. N for No: ").lower()
			if user_input == 'y':
				user_cards.append(deal_card())
			else: 
				is_game_over = True

	while computer_score != 0 and computer_score < 17:
		computer_cards.append(deal_card())
		computer_score = get_total(computer_cards)

	print(f"\nYour final hand: {user_cards}, final score: {user_score}")
	print(f"\nComputer's final hand: {computer_cards}, final score: {computer_score}")
	print(compare(user_score, computer_score))


	while input("\n\nDo you want to play a game of Blackjack? Y for Yes, N for No: ").lower() == 'y':
		play_game()

play_game()
