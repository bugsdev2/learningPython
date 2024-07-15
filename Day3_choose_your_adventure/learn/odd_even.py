def is_odd_or_even(num):
	if num % 2 == 0:
		print(f"{num} is even.")
	else:
		print(f"{num} is odd.")


print("Odd or Even")
number = int(input("Enter the number: "))
is_odd_or_even(number)

