from calculator_art import logo

def add(n1, n2):
	return n1 + n2
	
def substract(n1, n2):
	return n1 - n2

def multiply(n1, n2):
	return n1 * n2
	
def divide(n1, n2):
	if n2 == 0:
		return "You cannot divide a number by zero."
	return n1 / n2

def calculate(num1, num2, operator):
	if operator == '+':
		return add(num1, num2)
	elif operator == '-':
		return substract(num1, num2)
	elif operator == '*':
		return multiply(num1, num2)
	elif operator == '/':
		return round(divide(num1, num2), 2)
	else:
		return "The operator you have entered is invalid." 


def calculator():
	print(logo)
	stop_running = False
	num1 = float(input("What is the first number? "))
	while not stop_running:
		print("+, -, *, /")
		operator = input("Pick an operator from above: ")
		num2 = float(input("What is the next number? "))
		result = calculate(num1, num2, operator)
		print(f"{num1} {operator} {num2} = {result}")
		user_input = input(f"Type 'Y' to continue operating with {result}, \n'N' to start a new calculation or \n'E' to end the calculator: ").lower()
		if user_input == 'y':
			num1 = result
			continue
		elif user_input == 'n':
			calculator()
		else: 
			return

calculator()
