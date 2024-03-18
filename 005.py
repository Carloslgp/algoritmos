print("--------------------------------")
print("-           Mulher - 1         -")
print("-           Homem - 2          -")
print("--------------------------------")
gen = int(input("Digite o respectivo número do seu gênero: "))
altura = float(input("Digite a sua altura em (M): "))
if gen == 1:
    peso = (62.1*altura)-44.7
    print("Seu peso ideal é : {:.1f}".format(peso))
elif gen == 2:
    peso = (72.7*altura)-58
    print("Seu peso ideal é : {:.1f}".format(peso))
else:
    print("ERRO")
    quit()
