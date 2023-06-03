def area(num1,num2,figura):
    if figura == "retangulo":
        area = num1 * num2
    elif figura == "losango":
        area = (num1 * num2)/2
    elif figura == "triangulo":
        area = (num1 * num2)/2
    elif figura == "circulo":
        area = num1 ** 2 * num2
    else:
        print("Algo de inesperado aconteceu")
    areaf = int(area)
    print(f"O {figura} tem {areaf} de area")
