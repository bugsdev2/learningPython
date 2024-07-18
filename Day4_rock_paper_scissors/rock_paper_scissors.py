import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]

def get_computer_choice():
	return options[random.randint(0, len(options) - 1 )]
	


def game_start():
	if user_input == "r":
		user_choice = rock
	elif user_input == "p":
		user_choice = paper
	elif user_input == "s":
		user_choice = scissors
	else:
		print("\n Sorry... This option does not exist! Try Again.")
		return
	
	computer_choice = get_computer_choice()
	
	if user_choice == computer_choice:
		print(f"\n Your choice: \n {user_choice} \n Computer's Choice: \n {computer_choice} \n The game is tied.")
		return
		
	if user_choice == rock and computer_choice == paper:
		print(f"\n Your choice: \n {user_choice} \n Computer's Choice: \n {computer_choice} \n You lose. Computer wins.")
		return
	elif user_choice == paper and computer_choice == rock:
		print(f"\n Your choice: \n {user_choice} \n Computer's Choice: \n {computer_choice} \n You win.")
		return
		
		
	if user_choice == paper and computer_choice == scissors:
		print(f"\n Your choice: \n {user_choice} \n Computer's Choice: \n {computer_choice} \n You lose. Computer wins.")
		return
	elif user_choice == scissors and computer_choice == paper:
		print(f"\n Your choice: \n {user_choice} \n Computer's Choice: \n {computer_choice} \n You win.")
		return
		
		
	if user_choice == scissors and computer_choice == rock:
		print(f"\n Your choice: \n {user_choice} \n Computer's Choice: \n {computer_choice} \n You lose. Computer wins.")
		return
	elif user_choice == rock and computer_choice == scissors:
		print(f"\n Your choice: \n {user_choice} \n Computer's Choice: \n {computer_choice} \n You win.")
		return
		
		
user_input = input("\n What do you choose? Rock, paper or scissors? \n Type in R, P or S: ").lower()
game_start()
	

