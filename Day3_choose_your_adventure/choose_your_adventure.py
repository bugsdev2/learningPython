print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("\n Welcome to Treasure Island.")
print("\n Your mission is to find the treasure. \n Be very careful with each step. \n You might either leave this game rich or leave it dead.") 

if input("\n Shall we begin? Y or N? ").lower() ==  "y":
	print("\n You are walking through a strange forest. \n It is night and you hear the howling of wolves. \n You soon come across a split in the path. \n One goes left, the other right. \n Both look equally eerie. But you have to make a decision.")
	if (input("\n Which path do you choose? Left or Right? ").lower() == "left"):
		print("\n You take the left path and you come across a river. \n It is a bit foggy but you could see some boulders scattered in river. \n The water seems to be calm and you are confident in your swimming abilities. \n But you are in a dilemma.")
		if input("\n Should you swim across or wait for some more time? Swim or Wait? ").lower() == "wait":
			print("\n You decide to wait. \n And thank God you did for as the fog slowly lifted, \n you are able to see way into the distance three boats. \n Each of a different colour: Yellow, Red and Blue.")
			boat_color = input("\n Which boat would you like to enter? Yellow, Red or Blue? ").lower()
			if boat_color  == "yellow":
				print(r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
               '-._'-.|| |' `_.-'
                    '-.||_/.-'
				''')
				print(f"\n You enter the {boat_color} boat and quickly rush over to the controls. \n Thank uncle Roger for teaching you how to ride a boat. \n You start the engine and make your way across \n where you see the treasure chest! \n Hurray! You have made it till the end. \n The treasure is now yours.")
			else:
				print(f"\n You choose the {boat_color} boat. \n As soon as you jump into the boat \n a trap door opens and you fall right into the river \n where amidst the fishes you also see large bodied reptiles \n moving closer to you. \n GAME OVER")
		else:
			print("\n You decide to swim across. \n You are very confident in your swimming abilites indeed \n but you failed to see that the floating piles of rocks \n  are actually crocodiles. \n You start to panic and multiple crocodiles move in closer to you... \n GAME OVER")
	else:
		print("\n You take the right path but find out that \n it wasn't the right path as soon as you see \n a bunch of hungry wolves staring at you menacingly \n with blood-shot eyes. You start to scream but it is useless. \n GAME OVER")
else:
	print("\n Too scared to play, are you? It's okay. \n You can come back after you've gathered some courage.")
