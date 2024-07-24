

def is_prime(num):
	i = 2
	if num == 0 or num == 1:
		return f"{num} is not a prime number"
		
	if num == 2:
		return f"{num} is a prime number"
	
	while i != num:
		if num % i == 0:
			return f"{num} is not a prime number"
		i += 1
	
	return f"{num} is a prime number"
		
	
print(is_prime(0))
print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(11))
print(is_prime(16))
print(is_prime(19))
print(is_prime(20))
print(is_prime(21))
print(is_prime(97))
print(is_prime(102))
