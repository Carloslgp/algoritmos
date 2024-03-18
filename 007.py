idade = int(input("Digite a sua idade: "))
if idade <= 15:
    print("Acesso negado")
else:
    peso = float(input("Digite a seu peso em (KG): "))
    if peso > 120:
        print("acesso negado")
    else:
        print("Liberado")
        