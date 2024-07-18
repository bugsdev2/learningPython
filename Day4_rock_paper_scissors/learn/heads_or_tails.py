import random

def coin_toss():
	if random.random() < 0.5:
		return 'Heads'
	else:
		return 'Tails'
		
		

print(coin_toss())
		
