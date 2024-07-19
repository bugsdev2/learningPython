student_heights = input("Input a list of student height seperated by a space: ").split()

for n in range(0, len(student_heights)):
	student_heights[n] = int(student_heights[n])

print(student_heights)

total = 0
count = 0
for height in student_heights:
	total += height
	count += 1
	
avg_height = total / count

print(f"The average height of the students is {round(avg_height, 2)}")
