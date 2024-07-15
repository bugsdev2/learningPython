def calc_time_left(age):
	age_int = int(age)
	years_left = 90 - age_int
	months_left = years_left * 12
	weeks_left = years_left * 52
	days_left = years_left * 365
	return f"Assuming you live upto the age of 90, you have {days_left} days or {weeks_left} weeks or {months_left} months left."
	

age_input = input("Enter your age: ")
print(calc_time_left(age_input))
