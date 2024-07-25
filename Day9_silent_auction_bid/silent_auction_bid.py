from silent_auction_bid_art import logo
import os


bidders = []

retry = True
while retry:
	os.system('clear')
	print(logo)
	print('Welcome to the Secret Audition Program')
	name = input("What is your name? ")
	bid_amt = int(input("What is your bid? "))
	new_bidder = {}
	new_bidder['name'] = name
	new_bidder['bid'] = bid_amt
	bidders.append(new_bidder)
	
	retry_input = input('Are there any other bidders? Y or N?: ').lower()
	if retry_input != 'y':
		retry = False

max_bidder = {
	'name': "",
	'bid': 0
}
for bidder in bidders:
	if bidder['bid'] > max_bidder['bid']:
		max_bidder['name'] = bidder['name']
		max_bidder['bid'] = bidder['bid']
	
print(f"\nThe winner is {max_bidder['name']} with a bid of Rs.{max_bidder['bid']}")
