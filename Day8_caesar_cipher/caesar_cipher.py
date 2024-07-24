from caesar_art import art
import re

print(art)
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("Caesar Cipher")

retry = True
while retry:
	direction = input("Type in 'encode' to encode and 'decode' to decode the message: ").lower()
	message = input(f"Enter the message you would like to {direction}: ")
	shift = int(input(f"Enter the shift number: "))
		
	def caesar(message, shift, direction):
		output_msg = ""
		if shift > 26:
			shift = shift % 26
		for letter in message:
			if re.match('[a-zA-Z]', letter):
				position = alphabet.index(letter)
				if direction == 'encode':
					output_msg += alphabet[position + shift]
				elif direction == 'decode':
					output_msg += alphabet[position - shift]
				else:
					print("Brother eww... Ewww brother...")
			else:
				output_msg += letter
		return output_msg

	print(f"Your {direction}d message is {caesar(message, shift, direction)}")

	retry_input = input("Do you want to encode/decode another message? Y or N? ").lower()
	if retry_input == 'n':
		retry = False
