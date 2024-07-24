alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("Caesar Cipher")
direction = input("Type in 'encode' to encode and 'decode' to decode the message: ").lower()
message = input(f"Enter the message you would like to {direction}: ")
shift = int(input(f"Enter the shift number: "))

# ~ def encode(message, shift):
	# ~ encoded_msg = ""
	# ~ for letter in message:
		# ~ position = alphabet.index(letter)
		# ~ encoded_msg += alphabet[position + shift]
	# ~ return encoded_msg
	
# ~ def decode(message, shift):
	# ~ decoded_msg = ""
	# ~ for letter in message:
		# ~ position = alphabet.index(letter)
		# ~ decoded_msg += alphabet[position - shift]
	# ~ return decoded_msg
	
# ~ if direction == 'encode':
	# ~ print(f"Your encoded message is: {encode(message, shift)}")
# ~ elif direction == 'decode':
	# ~ print(f"Your decoded message is: {decode(message, shift)}")
# ~ else:
	# ~ print("Do you even know how to read?")
	
	
def caesar(message, shift, direction):
	output_msg = ""
	for letter in message:
		position = alphabet.index(letter)
		if direction == 'encode':
			output_msg += alphabet[position + shift]
		elif direction == 'decode':
			output_msg += alphabet[position - shift]
		else:
			print("Brother eww... Ewww brother...")
	return output_msg

print(f"Your {direction}d message is {caesar(message, shift, direction)}")
