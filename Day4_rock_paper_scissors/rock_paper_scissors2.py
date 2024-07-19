# This was in the solution given in the course and I felt that this game logic is very simple and effective as well compared to mine which had loads of repetitions and stuff.
# Nice. I must try to think in terms of numbers whenever and where ever it can be applied. So cool!

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

user_choice = int(input("\n What do you choose? Type in 0 for rock, 1 for paper, and 2 for scissors: "))

if user_choice > 2 or user_choice < 0:
	print("You have entered an invalid number. You lose.")
else:
	computer_choice = random.randint(0, 2)
	
	print(f"Your choice: \n {options[user_choice]} \n Computer's choice: \n {options[computer_choice]}")
	
	if user_choice == 0 and computer_choice == 2:
		print("You win.")
	elif computer_choice == 0 and user_choice == 2:
		print("You lose.")
	elif computer_choice > user_choice:
		print("You lose. Computer wins.")
	elif user_choice > computer_choice:
		print("You win.")
	elif user_choice == computer_choice:
		print("The game is tied.")
