# true = cartão vencido
def confere(mes1,ano1,mes2,ano2):
    if ano2 < ano1:
        return True
    elif ano2 == ano1:
        if mes2 < mes1:
            return True
        else:
            return False
    else:
        return False
	
print(confere(4,2012,5,2012))