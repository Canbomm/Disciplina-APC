pop_a,pop_b,perc_a,perc_b = input().split()
pop_a = int(pop_a)
pop_b = int(pop_b)
cresc_a = (float(perc_a)/100) + 1
cresc_b = (float(perc_b)/100) + 1

def alcanca(pop_a,pop_b,cresc_a,cresc_b):
	# definindo caso base
	# A nunca alcanca B
	if cresc_b >= cresc_a:
		return "A nunca alcancara B."
	
	# simulando os anos passando
	alcanca = 0
	while pop_a < pop_b:
		pop_a = int(pop_a * cresc_a)
		pop_b = int(pop_b * cresc_b)
		alcanca += 1
		if alcanca == 1000:
			return "Mais de um milenio."
	return f"Vai alcancar em {alcanca} ano(s)."

print(alcanca(pop_a,pop_b,cresc_a,cresc_b))
