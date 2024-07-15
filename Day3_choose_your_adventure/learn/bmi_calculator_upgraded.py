def calc_bmi(height, weight):
	bmi = round(int(weight) / float(height) ** 2)
	if bmi < 18.5:
		print(f"Your BMI is {bmi}. You are underweight.")
	elif bmi < 25: 
		print(f"Your BMI is {bmi}. You have a normal weight.")
	elif bmi < 30:
		print(f"Your BMI is {bmi}. You are overweight.")
	elif bmi < 35:
		print(f"Your BMI is {bmi}. You are obese.")
	else:
		print(f"Your BMI is {bmi}. You are clinically obese.")

print("BMI CALCULATOR")
height_input = input("Enter your height: ")
weight_input = input("Enter your weight: ")

calc_bmi(height_input, weight_input)
