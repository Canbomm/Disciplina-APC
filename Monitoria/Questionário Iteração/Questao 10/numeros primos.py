def ehPrimo(num):
	if num > 1:
		teste = 2
		while teste < num:
			if num % teste == 0:
				return 0
			teste += 1
		return 1
	else:
		return 0

def divisoresPrimos(num):
	divisor = 0
	total_divisores = 0
	while divisor < num:
		if ehPrimo(divisor):
			if num % divisor == 0:
				total_divisores += 1
		divisor += 1
	return total_divisores
