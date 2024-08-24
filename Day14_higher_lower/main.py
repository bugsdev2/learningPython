from art import logo, vs
from game_data import data
import random
import os


def get_person_details():
	persons = []
	for _ in range(2):
		persons.append(random.choice(data))
	while persons[0] == persons[1]:
		persons[1] = random.choice(data)
	return persons
	
	
def compare(guess, A, B):
	if A['follower_count'] < B['follower_count']:
		return 'b'
	else:
		return 'a'



print(logo)
print('Welcome to Higher or Lower!')
user_input = input("\nDo you want to start the game? Y or N: ").lower()
if user_input == 'y':
	is_game_start = True
else:
	is_game_start = False

score = 0
[A, B]= get_person_details()
while is_game_start:
	
	# ~ print(logo)
	A = B
	B = random.choice(data)
	# ~ print(f"Current Score: {score}")
	print(f"\nCompare A: {A['name']}, a {A['description']} from {A['country']}")
	print(vs)
	print(f"Against B: {B['name']}, a {B['description']} from {B['country']}")
	guess = input("Who has more followers? A or B: ").lower()
	
	os.system('cls' if os.name == 'nt' else 'clear')
	
	if guess == compare(guess, A, B):
		score += 1
		print(f"You're right! Current Score: {score}")
	else:
		print(f"\nSorry. It was the wrong answer. You lose this game.")
		print(f"Final Score: {score}")
		is_game_start = False
			
	
	



