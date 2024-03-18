print("###############################")
print("#        PUCPR - 1            #")
print("#       UNICAMP - 2           #")
print("###############################")
uni = int(input("Digite o respectivo número de seu faculdade: "))
n1 = float(input("Qual a sua primeira nota? "))
n2 = float(input("Qual a sua segunda nota? "))
media = (n1+n2)/2
if uni == 1:
    if media >= 7:
        print("aprovado")
    elif 4 <= media < 7:
        print("Recuperação")
    else:
        print("Reprovado")
elif uni == 2:
    if media >= 5:
        print("aprovado")
    else:
        print("Reprovado")
else:
    print("reprovado")
