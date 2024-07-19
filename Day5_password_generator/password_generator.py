import random

letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

print("Welcome to the Password Generator")

letter_count = int(input("How many letters would you like to have in your password? \n"))
number_count = int(input("How many numbers would you like to have in your password \n"))
symbol_count = int(input("How many symbols would you like to have in your password? \n"))

password = ""

random_letters = ""
random_numbers = ""
random_symbols = ""

for n in range(1, letter_count+1):
	random_letters += letters[random.randint(0, len(letters) - 1)]
	
for n in range(1, number_count+1):
	random_numbers += numbers[random.randint(0, len(numbers) - 1)]
	
for n in range(1, symbol_count+1):
	random_symbols += symbols[random.randint(0, len(symbols) - 1)]


password = random_letters+random_numbers+random_symbols
## Easy Password Generator
print(f"Your password could be: \n{password}")

password_list = [letter for letter in password]

random.shuffle(password_list)

print(f"\nBut here's a better version: \n{''.join(password_list)}")

		
