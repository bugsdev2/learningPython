student_heights = [78, 65, 89, 86, 55, 91, 65, 89]

max_height = 0
for height in student_heights:
	if height > max_height:
		max_height = height


min_height = max_height

for height in student_heights:
	if height < min_height:
		min_height = height


print(f"The maximum height is {max_height}. The minimun height is {min_height}")

	
