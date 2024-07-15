def calc_bmi(height, weight):
	bmi = int(float(weight) / float(height) ** 2)
	return bmi
	

height_input = input("Enter your height in m: ")
weight_input = input("Enter your weight in kg: ")

print(calc_bmi(height_input, weight_input))
