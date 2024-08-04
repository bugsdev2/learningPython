from blackjack_art import logo
import random

cards = [ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10 ]

def get_additional_card(cards):
	cards.append(random.choice(cards))
		
def get_total(cards):
	total = 0
	for card in cards:
		total += card
	return total

	

def get_two_cards():
	return [random.choice(cards), random.choice(cards)]
	
	
def start_game():
	user_cards = get_two_cards()
	computer_cards = get_two_cards()
	
		
	print(f"Your cards: {user_cards}")
	print(f"Computer's first card: {computer_cards[0]}")
	player_input = input("Type 'y' to pull another card, type 'n' to pass: ").lower()
	
	if player_input == 'y':
		get_additional_card(user_cards)
		user_total = get_total(user_cards)
		print(user_cards, computer_cards)
		if user_total > 21 and 11 in user_cards:
			cards[cards.index(11)] = 1
		
		print(user_cards, computer_cards)
	

print(logo)
start_game_input = input("\nDo you want to play a game of blackjack? Y or N? ").lower()

if start_game_input == 'y':
	start_game()
	

