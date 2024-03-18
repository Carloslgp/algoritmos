idade = int(input("Digite a sua idade: "))
tempo = int(input("Digite o seu tempo de serviço: "))
if idade >= 65 or tempo>= 30:
    print("Pode se aposentar")
elif 65 >= idade >= 60 and tempo >=25:
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")
