def is_leap_year(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				print(f"{year} is a leap year.")
			else:
				print(f"{year} is not a leap year.")
		else:
			print(f"{year} is a leap year.")
	else:
		print(f"{year} is not a leap year.")
		

print("Leap Year Check")
year_input = int(input("Enter the year: "))

is_leap_year(year_input)
