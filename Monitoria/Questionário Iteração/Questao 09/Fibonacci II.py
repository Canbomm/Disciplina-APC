def calcula_fibo(num):
	if num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		return calcula_fibo(num-1) + calcula_fibo(num-2)

def fibonacci(num):
	sequencia = 0
	while sequencia < num:
		print(calcula_fibo(sequencia),end=" ")
		sequencia += 1
	print()
