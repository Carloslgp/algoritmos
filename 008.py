idade = int(input("Digite a sua idade: "))
if idade < 16:
    print("Não é eleitor")
elif 16 <= idade < 18 or idade >65:
    print("Eleitor facultativo")
else:
    print("Eleitor obrigatório")
