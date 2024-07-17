print("Welcome to the Love Calculator!")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

combined_name = name1 + name2

t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')

true_count =  t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love_count = l + o + v + e

final_score = int(str(true_count) + str(love_count))

if final_score < 10 or final_score > 90:
	print(f"Your score is {final_score}. You go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
	print(f"Your score is {final_score}. You are alright together.")
else:
	print(f"Your score is {final_score}")

