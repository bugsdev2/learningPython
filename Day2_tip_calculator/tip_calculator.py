def calc_tip_per_person(total, tip, persons):
	# ~ basically instead of doing bill amount + (bill amount * tip percent (12/100 = .12)), 
	# ~ we do bill amount * 1 + 0.12 => 1.12 to get total.
	tip_ease = "1." + tip 
	# ~ "{:.2f}".format(***) is used to round to two decimal places proper
	return "{:.2f}".format((float(total) * float(tip_ease) ) / int(persons), 2)

print("Tip Calculator")
bill_amount = input("Enter the total bill: Rs.")
tip_amount = input("How much would you like to tip? 12, 15, 18? ")
person_count = input("How many people are splitting the bill? ")

each_person_amount = calc_tip_per_person(bill_amount, tip_amount, person_count)

print(f"Each person has to pay Rs.{each_person_amount}/-")

