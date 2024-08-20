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
	

player_cards = get_two_cards()
computer_cards = get_two_cards()



def start_game():
	print(f"\nYour cards: {player_cards}")
	print(f"\nComputer's first card: {computer_cards[0]}")
	player_total = get_total(player_cards)
	computer_total = get_total(computer_cards)
	
	if computer_total == 21:
		print(f"\nComputer's cards: {computer_cards}")
		print("\nYou lose")
	
	if player_total == 21:
		print(f"\nComputer's cards: {computer_cards}")
		print("\nYou win")
	elif player_total > 21 and 11 in player_cards:
		player_cards[player_cards.index(11)] = 1
		player_total = get_total(player_cards)
		if player_total > 21:
			print(f"\nComputer's cards: {computer_cards}")
			print("\nYou lose")
	elif player_total > 21:
		print(f"\nComputer's cards: {computer_cards}")
		print("\nYou lose")
	else:
		user_action = input("\nDo you want to draw another card or wait? Y to Pick. N to Wait: ").lower()
		if user_action == 'y':
			get_additional_card(player_cards)
			start_game()
		else:
			while computer_total < 17:
				get_additional_card(computer_cards)
				computer_total = get_total(computer_cards)
				if computer_total > 21:
					print(f"\nComputer's cards: {computer_cards}")
					print("\nYou win")
				else:
					if computer_total < player_total:
						print(f"\nComputer's cards: {computer_cards}")
						print("\nYou win")
					elif computer_total > player_total:
						print(f"\nComputer's cards: {computer_cards}")
						print("\nYou lose")
					else: 
						print(f"\nComputer's cards: {computer_cards}")
						print("Draw")
	

start_game()
